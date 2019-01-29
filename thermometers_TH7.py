#! /usr/bin/python
import sys
import time
import Tkinter	# requires python-tk (apt-get install python-tk)
from Tkinter import *
import random
import math
import os
import spidev
import time
import RPi.GPIO as GPIO

#
# TH7 thermocouple reader for the raspberry pi
#
# The array below `temps' holds the temperatures calculated
# in centigrade
#
temps = [ 20.3,20.3,20.3,20.3,20.3,20.3,20.3 ]

# start of the thermometers at bottom of page
ybase = 600

# set up the I/O to read the thermocouples
#
spi = spidev.SpiDev()  # spi instance to read 12 bit ADC	
spi_tc77 = spidev.SpiDev() # spi instance to read TC77 digital temperature chip
spi.open(0, 0)
spi_tc77.open(0,1)
spi.max_speed_hz =  10000
spi_tc77.max_speed_hz =  10000
# create spi object
# open spi port 0, device (CS) 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT) # D2 LED   
GPIO.setup(17, GPIO.OUT) # D3 LED
GPIO.output(22,GPIO.HIGH) # D2 LED OFF
GPIO.output(17,GPIO.LOW) # D3 LED ON
led_counter=0
pcb_temp = 25.0
channels = [0,0,0,0,0,0,0,0]
vadj =1.0
vadj_now=1.0
vref=0.0
# compress movement for thermometers
#

def tcompress ( t ):
   if t < -55:
      t = ((t+55)/5 - 55)
   if t > 120:
      t = (t/5 + 96)
   return t



# assume kelvin input
#
def tcompressk ( t ):
    return tcompress(t -273.15)*2

# print the micro-volts, voltage supplied to pi and the voltage adjustment factors
# onto a terminal
#
def print_list():
    global pcb_temp
    for i in range(1, len(channels)):
        uv = channels[i] + (k_type_translate_c(pcb_temp))
        if uv < -6500:
          print ('channel: %d\t %.3f uV \t %.3f oC (K-type) ERROR' % (i, uv, k_type_translate_uv(uv))) 
        else:
          print ('channel: %d\t %.3f uV \t %.3f oC (K-type)' % (i, uv, k_type_translate_uv(uv)))
        temps[i-1] = k_type_translate_uv(uv) # for the gui thermomemters
    print "vadj:    \t%2f" % vadj
    print "vadj_now: %2f  Pi Vdd %f" % (vadj_now, 5.0/vadj)
    #print "PCB_TEMP: %2f" % pcb_temp
    print "PCB_TEMP %2foC uV:\t%2f\t(%2f C)" % (pcb_temp,k_type_translate_c(pcb_temp), k_type_translate_uv(k_type_translate_c(pcb_temp)))


# ITS-90 thermocouple polynomial equations to translate temperature oC to microvolts
# for `k' type thermocouples
#
#
def k_type_translate_c(temp):
    c0 =  c1 =  c2 =  c3 =  c4 =  c5 =  c6 =  c7 =  c8 =  c9 =  c10 = 0.0
    t = et = mikrovolts = 0.0

    a0 = 1.185976e2
    a1 = -1.183432e-4

    if (temp < 0.0):
        c0 = 0.0
        c1 = 3.9450128025e1
        c2 = 2.3622373598e-2
        c3 = -3.2858906784e-4
        c4 = -4.9904828777e-6
        c5 = -6.7509059173e-8
        c6 = -5.7410327428e-10
        c7 = -3.1088872894e-12
        c8 = -1.0451609365e-14
        c9 = -1.9889266878e-17
        c10 = -1.6322697486e-20
        et = 0.0
    
    elif(temp >= 0.0 and temp < 13720.0):
        c0 = -1.7600413686e1
        c1 = 3.8921204975e1
        c2 = 1.8558770032e-2
        c3 = -9.9457592874e-5
        c4 = 3.1840945719e-7
        c5 = -5.6072844889e-10
        c6 = 5.6075059059e-13
        c7 = -3.2020720003e-16
        c8 = 9.7151147152e-20
        c9 = -1.2104721275e-23
        c10 = 0.0
        t = (temp)
        t -= 126.9686
        t = t * t
        t = t * a1
        et = math.exp(t) * a0
    else:
        return 0.0
    t = (temp)
    mikrovolts = c0 + t * (c1 + t * (c2 + t * (c3 + t * (c4 + t * (c5 + t * (c6 + t * (c7 + t * (c8 + t * (c9 + t * (c10)))))))))) + et
    return mikrovolts

# ITS-90 k type thermocouple function to translate microvolts to temperature
def k_type_translate_uv(uV):
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = 0.0
    temp = 0.0
    if (uV >= -5891.0 and uV < 0.0):
        c0 = 0
        c1 = 2.5173462e-2
        c2 = -1.1662878e-6
        c3 = -1.0833638e-9
        c4 = -8.9773540e-13
        c5 = -3.7342377e-16
        c6 = -8.6632643e-20
        c7 = -1.0450598e-23
        c8 = -5.1920577e-28
        c9 = 0

        temp = c0 + uV * (c1 + uV * (c2 + uV * (c3 + uV * (c4 + uV * (c5 + uV * (c6 + uV * (c7 + uV * (c8))))))))
    elif (uV >= 0.0 and uV < 20644.0):
        c0 = 0
        c1 = 2.508335e-2
        c2 = 7.860106e-8
        c3 = -2.503131e-10
        c4 = 8.315270e-14
        c5 = -1.228034e-17
        c6 = 9.804036e-22
        c7 = -4.413030e-26
        c8 = 1.057734e-30
        c9 = -1.052755e-35
        
        temp = c0 + uV * (c1 + uV * (c2 + uV * (c3 + uV * (c4 + uV * (c5 + uV * (c6 + uV * (c7 + uV * (c8 + uV * (c9)))))))))


    elif (uV >= 20644.0 and uV < 54886.0):
        c0 = -1.318058e2
        c1 = 4.830222e-2
        c2 = -1.646031e-6
        c3 = 5.464731e-11
        c4 = -9.650715e-16
        c5 = 8.802193e-21
        c6 = -3.110810e-26
        c7 = 0
        c8 = 0
        c9 = 0

        temp = c0 + uV * (c1 + uV * (c2 + uV * (c3 + uV * (c4 + uV * (c5 + uV * (c6))))))
    else:
        temp = -300.0 # OUT OF RANGE deliberately
    return temp




a = 0
ch1_uv = 0.0
result=0

def read_thermocouples():
  # try:
    global a
    global vref
    global vadj
    global led_counter
    global pcb_temp
    a = a + 1
    if a>8:
      os.system("clear") # this is for tunning in a terminal over ssh on a pi
      a = 0
      print_list()
      #time.sleep(0.1)

    time.sleep(0.01)
    # perpare bits for ADC command to read channel 
    cb1 = 4 + 2 + ((a & 4) >> 2)
    cb2 = (a & 3) << 6
    resp = spi.xfer2([cb1, cb2, 0x00])

    if a == 0:
        vref = resp[1] * 256.0 + resp[2] * 1.0
        vadj_now = vref/3355.4432
        vadj = vadj_now * 0.1 + vadj * 0.9
        print "vref: ", vref, "vadj: ", vadj
        channels[a] = vref

        if led_counter<4: 
          GPIO.output(17,GPIO.LOW) # D3 LED ON
          GPIO.output(22,GPIO.HIGH) # D2 LED OFF
        else:
          GPIO.output(17,GPIO.HIGH) # D3 LED OFF
          GPIO.output(22,GPIO.LOW) # D2 LED ON
        led_counter = led_counter + 1
        if led_counter>8:
           led_counter=0
    if a >= 1 and a < 8:
        ch1_adc12_5v = ((resp[1] * 256.0 + resp[2]*1.0) - vref) * vadj
        ch1 = resp[1] * 256.0 + resp[2]*1.0
        perfect = ((vref - ch1) * vadj)
        bigV = (perfect/4096.0)*5.0
        # the signal has been amplified G=100 so we need to multiply by 10K
        uV = bigV*10000
        # now first order filter the micro-volts to reduce random noise
        channels[a] = channels[a]*0.9 + 0.1*uV
    if a == 8: # read the temperature from the tc77
    	resp = spi_tc77.xfer2([0x00, 0x00, 0x00, 0x00]) # transfer four bytes
        number = resp[0] * 256 + resp[1]
	pcb_temp = (number/8.0) * 0.0625
	print "Temp: ", pcb_temp, resp

# set up the gui
#
curtime = ''
curtemp = ''
newtemp = -299.0
timeline = [1,2,3,4,5,6,7]
templine = [1,2,3,4,5,6,7]
templine2 = [1,2,3,4,5,6,7]
timeobj = ''
abs_zero = -273.15


class Window:

  def __init__(self,root):
    self.root = root 
    self.canvas = Tkinter.Canvas(self.root)
    self.canvas.pack()
    self.canvas.config(background='lightblue')
    self.canvas.config(width=500)
    self.canvas.config(height=900)


class TH7gui():
	device = None
	handle = None
	def __init__(self,):
		return None

	def open(self):
		return self.handle

update_gui_counter = 0

def update_gui():
  INTERVAL = 1
  global curtime
  global curtemp
  global timeobj
  global newtemp
  global ybase
  global update_gui_counter
  deg = unichr(176).encode("utf-8")
  read_thermocouples()
  update_gui_counter = update_gui_counter + 1
  #print "update_gui_counter", update_gui_counter
  if update_gui_counter >= 10:
    update_gui_counter  = 0 
    for i in range(7):
            #
            #print 'newtemp' , newtemp
            newtemp = temps[i]
            temps[i] += 0.1 * random.randrange(-10, 20)
            if temps[i] > 500:
                temps[i] = -300
            
            if templine2:
              TH7_window.canvas.delete(templine2[i])
              TH7_window.canvas.delete(templine[i])
            t1 = " %2.2d " % newtemp
            kelvin = newtemp + (-abs_zero);
            
            
            if kelvin >= 273.15 + 40:
              filc = 'pink' # warm
            if kelvin >= 273.15 + 70: # 120oC
              filc = 'red' # hot
            if kelvin < 273.15 + 35:
              filc = 'orange' # human levels of body temperature, go orange
            if kelvin < 273.15 + 24:
              filc = 'grey' # coldish
            if kelvin < 273.15:
              filc = 'blue' # cold
            if kelvin < -15+273.15:
              filc = 'black' # very very cold, like sweden in the winter cold
            
            x1 = 115 + i * 50
            x2 = 125 + i * 50
            y1 =  (ybase)
            y2 = (ybase)-tcompressk(kelvin)
            #y2 =  (ybase)-kelvin
            #print " x1 ",x1, " y1 ", y1, " x2 ", x2, " y2 ", y2
            templine[i] = TH7_window.canvas.create_text(x1, y1+250, text=t1, font=("Helvetica", "12", "bold"), fill='green')
            templine2[i] = TH7_window.canvas.create_rectangle(x1, y1, x2,  y2, fill=filc)
            
            #tll = TH7_window.canvas.create_oval( x1-15, 800+30, x1+25, 800, fill=filc)
    
    #
    #
    y1pos = ybase - tcompressk(0.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="-273.15", font=("Helvetica", "18", "bold"), fill='black') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15-200.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="-200oC", font=("Helvetica", "18", "bold"), fill='blue') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15-100.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="-100"+deg+"C", font=("Helvetica", "18", "bold"), fill='blue') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15-0.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="-0oC", font=("Helvetica", "18", "bold"), fill='black') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+100.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="100oC", font=("Helvetica", "18", "bold"), fill='black') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+200.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="200oC", font=("Helvetica", "18", "bold"), fill='red') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+300.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="300oC", font=("Helvetica", "18", "bold"), fill='red') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+400.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="400oC", font=("Helvetica", "18", "bold"), fill='red') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+600.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="600oC", font=("Helvetica", "18", "bold"), fill='red') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
    #
    y1pos = ybase - tcompressk(273.15+800.0)
    templine3 = TH7_window.canvas.create_text ( 55, y1pos, text="800oC", font=("Helvetica", "18", "bold"), fill='red') 
    templine4 = TH7_window.canvas.create_line ( 55, y1pos, 700, y1pos, fill='grey')
  
    # get time
    newtime = time.strftime('%y:%m:%d::%H:%M:%S')
    if newtime != curtime:
      curtime = newtime
    #if timeobj:
    #  TH7_window.canvas.delete(time_obj)
    #timeobj = TH7_window.canvas.create_text(400, 40, text=curtime, font=("Helvetica", "48", "bold"), fill='red')
  
  # recall every 10ms but only draw every tenth
  TH7_window.canvas.after(INTERVAL, update_gui)

if __name__ == "__main__":
	root = Tkinter.Tk()
	root.title('TH7 Thermometer Display')
	TH7_window = Window(root)
	update_gui()
	root.mainloop()


