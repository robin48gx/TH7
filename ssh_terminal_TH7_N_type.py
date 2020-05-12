#!/usr/bin/python

import math
import os
import spidev
import time
import datetime
import RPi.GPIO as GPIO
import logging
from n_type import n_uv_to_c, n_c_to_uv
from j_type import j_uv_to_c, j_c_to_uv

dt = datetime.datetime.now()
logging.basicConfig(filename='TH7.log',level=logging.DEBUG)
#logging.info('So should this')
logging.warning('TH7 LOG FILE STARTED ' + dt.__str__())


old_min = datetime.datetime.now().minute
#
# TH7 thermocouple reader for the raspberry pi
#
# This program displays corrected micro-volts
# and temperatures for seven `k' type thermocouples
# on a terminal or ssh terminial.
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
first_run = 1
kk=0
pcb_temp = 25.0
channels = [0,0,0,0,0,0,0,0]
vadj =1.0
vadj_now=1.0
vref=0.0
def print_list():
    global old_min
    global logging
    print datetime.datetime.now()
    min = datetime.datetime.now().minute
    #print 'min %d' % ( min )

    piv = 5.0/vadj

    if piv < 4.8 or piv > 5.25:
         print "Voltage error\nCheck Raspberry Pi power supply."
         return



    if min != old_min:
      logging.info ( '-------- TH7 ---------------------' + datetime.datetime.now().__str__()  )

    for i in range(1, len(channels)):
        uv = channels[i] + (n_c_to_uv(pcb_temp))
        if uv < -6500:
          st = ('channel: %d\t %.3f uV \t %.3f oC (N-type) ERROR' % (i, uv, n_uv_to_c(uv))) 
        else:
          st = ('channel: %d\t %.3f uV \t %.3f oC (N-type)' % (i, uv, n_uv_to_c(uv)))
        print st
        if min != old_min:
            logging.info( st )
    vadjst = "vadj:    \t%2f" % vadj
    vadj2st =  "vadj_now: %2f  Pi Vdd %f" % (vadj_now, 5.0/vadj)
    #print "PCB_TEMP: %2f" % pcb_temp
    uvadj =  "PCB_TEMP %2foC uV:\t%2f\t(%2f C)" % (pcb_temp,n_c_to_uv(pcb_temp), n_uv_to_c(n_c_to_uv(pcb_temp)))
    print vadjst
    print vadj2st
    print uvadj
    if min != old_min:
        logging.info ( vadjst )
        logging.info ( vadj2st )
        logging.info ( uvadj )
        old_min = min

a = 0
ch1_uv = 0.0
result=0



while True:
  try:
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
        if first_run == 1:
            vadj = vadj_now
        vadj = vadj_now * 0.1 + vadj * 0.9
        print "vref: ", vref, "vadj: ", vadj
        channels[a] = vref

        if kk<4: 
          GPIO.output(17,GPIO.LOW) # D3 LED ON
          GPIO.output(22,GPIO.HIGH) # D2 LED OFF
        else:
          GPIO.output(17,GPIO.HIGH) # D3 LED OFF
          GPIO.output(22,GPIO.LOW) # D2 LED ON
        kk = kk + 1
        if kk>8:
           kk=0
    if a >= 1 and a < 8:
        ch1_adc12_5v = ((resp[1] * 256.0 + resp[2]*1.0) - vref) * vadj
        ch1 = resp[1] * 256.0 + resp[2]*1.0
        perfect = ((vref - ch1) * vadj)
        bigV = (perfect/4096.0)*5.0
        # the signal has been amplified G=100 so we need to multiply by 10K
        uV = bigV*10000
        # now first order filter the micro-volts to reduce random noise
        if first_run == 1:
           channels[a] = uV
        else:
           channels[a] = channels[a]*0.9 + 0.1*uV
    if a == 8: # read the temperature from the tc77
    	resp = spi_tc77.xfer2([0x00, 0x00, 0x00, 0x00]) # transfer four bytes
        number = resp[0] * 256 + resp[1]
        if first_run == 1:
          first_run = 0
	pcb_temp = (number/8.0) * 0.0625
	print "Temp: ", pcb_temp, resp

  except KeyboardInterrupt:
  # Ctrl+C pressed, so...
    spi_tc77.close()
    spi.close() # close the ports before exit

