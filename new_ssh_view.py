#!/usr/bin/python

import math
import os
import spidev
import time
import datetime
import RPi.GPIO as GPIO
import numpy as np
from thermocouples import * # bad practice but everything is properly namespaced.....

class Thermocouple_Channel:

    def __init__(self, channel, filter_level=0, thermocouple_type='uv', offset=0.0):

        self.channel = channel
        self.filter_level = filter_level
        self.thermocouple_type = thermocouple_type
        self.offset = offset # in C
        self.value_uv = 0.0
        self.temperature = 0.0
    


# conversion variables



thermocouples = np.array([0, 0, 0, 0, 0, 0, 0], dtype=object)

# initialise array/list with 7 "blanks"
for i in range(0, 7):
    thermocouples[i] = Thermocouple_Channel(i+1)

# channel 1...
thermocouples[0] = Thermocouple_Channel(1, 1, 'K')
# channel 2...
thermocouples[0] = Thermocouple_Channel(2, 0, 'N', -25.0)


# main "printing loop."

def print_list():

    print datetime.datetime.now()

    piv = 5.0/vadj

    if piv < 4.8 or piv > 5.25:
         print "Voltage error\nCheck Raspberry Pi power supply."
         return

    for i in range(0, len(thermocouples)): 
        print ("Channel %d; %.1f uV; temp=%.2f oC; Type=%s; [F=%d]" % \
            (thermocouples[i].channel, thermocouples[i].value_uv, thermocouples[i].temperature, thermocouples[i].thermocouple_type, thermocouples[i].filter_level))
          
    vadjst = "vadj:    \t%2f" % vadj
    vadj2st =  "vadj_now: %2f  Pi Vdd %f" % (vadj_now, 5.0/vadj)
    #print "PCB_TEMP: %2f" % pcb_temp
    uvadj =  "PCB_TEMP %2foC uV:\t%2f\t(%2f C)" % (pcb_temp, translate_celsius_to_uv(pcb_temp), translate_uv_to_celsius(translate_celsius_to_uv(pcb_temp)))
    print vadjst
    print vadj2st
    print uvadj


spi = spidev.SpiDev()  # spi instance to read 12 bit ADC	
spi_tc77 = spidev.SpiDev() # spi instance to read TC77 digital temperature chip
spi.open(0, 0)
spi_tc77.open(0,1)
spi.max_speed_hz =  10000
spi_tc77.max_speed_hz =  10000
# create spi object
# open spi port 0, device (CS) 0

first_run = 1

pcb_temp = 25.0
vadj =1.0
vadj_now=1.0
vref=0.0

a = 0
result=0



while True:
  try:
    a = a + 1
    if a>8:
      os.system("clear") # this is for tunning in a terminal over ssh on a pi
      a = 0
      print_list()

    time.sleep(0.01)

    # prepare bits for ADC command to read channel 
    cb1 = 4 + 2 + ((a & 4) >> 2)
    cb2 = (a & 3) << 6
    resp = spi.xfer2([cb1, cb2, 0x00])

    # calculate vref and adjustment variables
    if a == 0:
        vref = resp[1] * 256.0 + resp[2] * 1.0
        vadj_now = vref/3355.4432
        if first_run == 1:
            vadj = vadj_now
        vadj = vadj_now * 0.1 + vadj * 0.9
        print "vref: ", vref, "vadj: ", vadj

    # read into thermocouple channels + apply adjustment and "lag filters"
    if a >= 1 and a < 8:

        # this variable is not referenced anywhere else?
        #ch1_adc12_5v = ((resp[1] * 256.0 + resp[2]*1.0) - vref) * vadj
        
        ch1 = resp[1] * 256.0 + resp[2]*1.0
        perfect = ((vref - ch1) * vadj)
        bigV = (perfect/4096.0)*5.0

        # the signal has been amplified G=100 so we need to multiply by 10K
        uv = bigV*10000


        # now first order filter the micro-volts to reduce random noise
        if first_run == 1:
            thermocouples[a-1].value_uv = uv
        else:
            thermocouples[a-1].value_uv = apply_lag_filter(thermocouples[a-1].value_uv, uv, thermocouples[a-1].filter_level) 


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


# first order filters of varying "hardness."
def apply_lag_filter(old_value, new_value, lag_level):
    if lag_level == 0:
        return new_value

    if lag_level == 1:
        return ( 0.9 * old_value + 0.1 * new_value )

    if lag_level == 2:
        return ( 0.95 * old_value + 0.05 * new_value )

    # this will change VERY slowly but probably be VERY stable...
    if lag_level == 3:
        return ( 0.995 * old_value + 0.005 * new_value )

#
def translate_uv_to_celsius(uv, tc_type='K'):
    
    uv = uv + 0.0

    if tc_type == 'K':
        return K_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == 'J':
        return J_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == 'N':
        return N_TYPE_TRANSLATE_UV_TO_C(uv)
# 
def translate_celsius_to_uv(c, tc_type='K'):

    c = c + 0.0

    if tc_type == 'K':
        return K_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == 'J':
        return J_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == 'N':
        return N_TYPE_TRANSLATE_C_TO_UV(c)


