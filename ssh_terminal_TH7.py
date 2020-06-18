#!/usr/bin/python

import math
import os
import spidev
import time
import datetime
import RPi.GPIO as GPIO
import numpy as np
import logging
from thermocouples import * # bad practice but everything is properly namespaced.....




dt = datetime.datetime.now()
logging.basicConfig(filename='TH7.log',level=logging.DEBUG)
logging.warning('TH7 LOG FILE STARTED ' + dt.__str__() + '\n')

class Thermocouple_Channel:

    def __init__(self, channel, filter_level=0, thermocouple_type="uv", offset=0.0):

        self.channel = channel
        self.filter_level = filter_level
        self.thermocouple_type = thermocouple_type
        self.offset = offset # in C COMING SOON!!
        self.value_uv = 0.0


# references/pointers to thermocouple_channel objects are stored here
thermocouples = np.array([0, 0, 0, 0, 0, 0, 0], dtype=object)

# initialise array/list with 7 "blanks"
for i in range(0, 7):
    # filter level = -1 indicates the channel is `blank'
    thermocouples[i] = Thermocouple_Channel(i+1, 2, "R", 0)



# Here, define each thermocouple channel connected to the TH7/ in use.
# 1st parameter is the No. of the channel; on PCB,
# 2nd is the filtering level, [0..3] (higher is harder filtering)
# 3rd is the T/C type as 1 upper-case character;
# currently supporting types: K, T, J, N, E, B, S


# channel, filter level, type, offset (in oC)

# channel 1...
thermocouples[0] = Thermocouple_Channel(1, 3, "K", 0.0)
# channel 2...
thermocouples[1] = Thermocouple_Channel(2, 3, "K",  2.0)
# channel 3...
thermocouples[2] = Thermocouple_Channel(3, 3, "K", 2.0 )
# channel 4...
thermocouples[3] = Thermocouple_Channel(4, 3, "K", 2.0)
# channel 5...
thermocouples[4] = Thermocouple_Channel(5, 3, "K", 2.0)
# channel 6...
#thermocouples[5] = Thermocouple_Channel(6, 3, "K")
# channel 7.
#thermocouples[6] = Thermocouple_Channel(7, 3, "K")




# first order filters of varying "hardness."
def apply_lag_filter(old_value, new_value, lag_level):
    if lag_level == 0 or lag_level == 1:
        return new_value

    if lag_level == 1:
        return ( 0.9 * old_value + 0.1 * new_value )

    if lag_level == 2:
        return ( 0.97 * old_value + 0.03 * new_value )

    if lag_level == 3:
        return ( 0.995 * old_value + 0.005 * new_value )

    # this will change VERY slowly but probably be VERY stable...
    if lag_level == 4:
        return ( 0.9995 * old_value + 0.0005 * new_value )

#
def translate_uv_to_celsius(uv, tc_type="K"):
    
    if uv is None:
        return -300.0
    
    uv = uv + 0.0

    if tc_type == "K":
        return K_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "J":
        return J_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "N":
        return N_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "T":
        return T_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "E":
        return E_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "B":
        return B_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "R":
        return R_TYPE_TRANSLATE_UV_TO_C(uv)
    if tc_type == "S":
        return S_TYPE_TRANSLATE_UV_TO_C(uv)

    if tc_type == "uv":
        return -300.0

    return -300.0
# 
def translate_celsius_to_uv(c, tc_type="K"):

    if c is None:
        return -300.0

    c = c + 0.0

    if tc_type == "K":
        return K_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "J":
        return J_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "N":
        return N_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "T":
        return T_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "E":
        return E_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "B":
        return B_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "R":
        return R_TYPE_TRANSLATE_C_TO_UV(c)
    if tc_type == "S":
        return S_TYPE_TRANSLATE_C_TO_UV(c)
    
    if tc_type == "uv":
        return -300.0


    return -300.0

# main "printing loop."

old_minute = datetime.datetime.now().minute
def print_list():

    global logging
    global old_minute
    dt = datetime.datetime.now()
    print dt
    minute = datetime.datetime.now().minute
    st = "" 
    piv = 5.0/vadj

    if piv < 4.8 or piv > 5.3:
         print "Voltage error\nCheck Raspberry Pi power supply."
         return

    for i in range(0, len(thermocouples)):

        tc_type = thermocouples[i].thermocouple_type
        f_level = thermocouples[i].filter_level
        channel = thermocouples[i].channel
        uv      = thermocouples[i].value_uv
        offset  = thermocouples[i].offset


        if uv is None:
            uv = -9000.0

        # the 'uV' field being printed does not factor in the 'estimated' pcb temp
        # however, the temperature field does and is in fact accurate.
        # to factor in the pcb temp in this field, rename "uv_with_pcb" to "uv".
        uv_with_pcb = uv + translate_celsius_to_uv(pcb_temp, tc_type)
        #uv_with_pcb = uv_with_pcb + translate_uv_to_celsius( translate_celsius_to_uv(offset, tc_type), tc_type)
        
        #print ("first_run %f"%first_run)        
        # lowest is J type at -8095 uv, others are lower but no one will be measuring -250 oC?
        if uv > -8100:
            st =  (("Channel %d: {:15.2f} uV, temp={:10.1f} oC, type=%-5s [F=%d]".format(uv, translate_uv_to_celsius(uv_with_pcb, tc_type)+offset) % (channel, tc_type, f_level)))
        else:
            st = ("Channel %d: DISCONNECT OR OPEN CIRCUIT" % channel)

        if uv > 38000: #38mV (for G=101)
            st = ("Chanel %d: ERROR HIGH" % channel)
        print st
        if (minute != old_minute):
            logging.info (st)
            #logging.info (dt)

    vadjst = ("vadj:    \t%2f" % (vadj))
    vadj2st =  "vadj_now: %2f  Pi Vdd %f" % (vadj_now, 5.0/vadj)
    #print "PCB_TEMP: %2f" % pcb_temp
    uvadj =  "PCB_TEMP %2foC uV:\t%2f\t(%2f C)" % (pcb_temp, translate_celsius_to_uv(pcb_temp), translate_uv_to_celsius(translate_celsius_to_uv(pcb_temp)))
    print vadjst
    print vadj2st
    print uvadj

    if ( minute != old_minute):
        #logging.info ( st )
        logging.info (vadjst)
        logging.info (vadj2st)
        logging.info (uvadj)
        logging.info (dt) # 1 timestamp per "section" is enough
        old_minute = minute

spi = spidev.SpiDev()  # spi instance to read 12 bit ADC	
spi_tc77 = spidev.SpiDev() # spi instance to read TC77 digital temperature chip
spi.open(0, 0)
spi_tc77.open(0,1)
spi.max_speed_hz =  10000
spi_tc77.max_speed_hz =  10000
# create spi object
# open spi port 0, device (CS) 0

first_run = 15

pcb_temp = 25.0
vadj =1.0
vadj_now=1.0
vref=0.0
ch1 = 0.0
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
        if first_run >= 0:
            vadj = vadj_now
        vadj = vadj_now * 0.1 + vadj * 0.9
        print "vref: ", vref, "vadj: ", vadj

    # read into thermocouple channels + apply adjustment and "lag filters"
    if a >= 1 and a < 8:

        # this variable is not referenced anywhere else?
        ch1_adc12_5v = ((resp[1] * 256.0 + resp[2]*1.0) - vref) * vadj
        
        ch1 = resp[1] * 256.0 + resp[2]*1.0
        perfect = ((vref - ch1) * vadj)
        bigV = (perfect/4096.0)*5.0

        # the signal has been amplified G=101 so we need to multiply by 10,100.00
        uv = bigV*10100


        # now first order filter the micro-volts to reduce random noise
        if first_run >= 0:
            # starts out every channel with the uv unfiltered
            thermocouples[a-1].value_uv = uv 
        else:
            thermocouples[a-1].value_uv = apply_lag_filter(thermocouples[a-1].value_uv, uv, thermocouples[a-1].filter_level) 


    if a == 8: # read the temperature from the tc77
    	resp = spi_tc77.xfer2([0x00, 0x00, 0x00, 0x00]) # transfer four bytes
        number = resp[0] * 256 + resp[1]
        if first_run >= 0:
          first_run = first_run - 1
	pcb_temp = (number/8.0) * 0.0625
	print "Temp: ", pcb_temp, resp

  except KeyboardInterrupt:
  # Ctrl+C pressed, so...
    spi_tc77.close()
    spi.close() # close the ports before exit
    # close db connection
    
