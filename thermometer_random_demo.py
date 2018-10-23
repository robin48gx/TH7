#! /usr/bin/python
import sys
import time
import Tkinter	# requires python-tk (apt-get install python-tk)
from Tkinter import *
import random


######################################################################
#
# Thermometer graphics demo in python / tkinter
#
# Tkinter graphics experiment to display some thermometers
#
# Uses random numbers so can be run without at TH7 installed
######################################################################

curtime = ''
curtemp = ''
newtemp = -299.0
timeline = [1,2,3,4,5,6,7]
templine = [1,2,3,4,5,6,7]
templine2 = [1,2,3,4,5,6,7]
timeobj = ''
abs_zero = -273.15

temps = [ -200, -273, -100, 100, 500, 400, 250 ]

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


def update_gui():
  INTERVAL = 100
  global curtime
  global curtemp
  global timeobj
  global newtemp
  deg = unichr(176).encode("utf-8")

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
            filc = 'pink'
          if kelvin >= 273.15 + 70: # 120oC
            filc = 'red'
          if kelvin < 273.15 + 40:
            filc = 'orange'
          if kelvin < 273.15 + 24:
            filc = 'grey'
          if kelvin < 273.15:
            filc = 'blue'
          if kelvin < -15+273.15:
            filc = 'black'
          
          x1 = 115 + i * 50
          x2 = 125 + i * 50
          y1 =  (800)
          y2 =  (800)-kelvin
          #print " x1 ",x1, " y1 ", y1, " x2 ", x2, " y2 ", y2
          templine[i] = TH7_window.canvas.create_text(x1, y1+50, text=t1, font=("Helvetica", "12", "bold"), fill='green')
          templine2[i] = TH7_window.canvas.create_rectangle(x1, y1, x2,  y2, fill=filc)
          
          tll = TH7_window.canvas.create_oval( x1-15, 800+30, x1+25, 800, fill=filc)
  
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-73.15, text="-200oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-73.15, 700, y1-73.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-173.15, text="-100"+deg+"C", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-173.15, 700, y1-173.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-273.15, text="-0oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-273.15, 700, y1-273.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-373.15, text="100oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-373.15, 700, y1-373.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-473.15, text="200oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-473.15, 700, y1-473.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-573.15, text="300oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-573.15, 700, y1-573.15, fill='grey')
  #
  templine3 = TH7_window.canvas.create_text ( 55, y1-673.15, text="400oC", font=("Helvetica", "18", "bold"), fill='black') 
  templine4 = TH7_window.canvas.create_line ( 55, y1-673.15, 700, y1-673.15, fill='grey')

  # get time
  newtime = time.strftime('%y:%m:%d::%H:%M:%S')
  if newtime != curtime:
    curtime = newtime
  #if timeobj:
  #  TH7_window.canvas.delete(time_obj)
  #timeobj = TH7_window.canvas.create_text(400, 40, text=curtime, font=("Helvetica", "48", "bold"), fill='red')

  # recall every 500ms
  TH7_window.canvas.after(INTERVAL, update_gui)

if __name__ == "__main__":
	root = Tkinter.Tk()
	root.title('TH7 Thermometer Display')
	TH7_window = Window(root)
	update_gui()
	root.mainloop()


