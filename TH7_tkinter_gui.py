#!/usr/bin/python3


# frame work for a tkinter GUI 
# to control/configure a TH7
# on a raspberry pi

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import spidev
from thermocouples import *
import numpy as np
import json
import os

DEFAULT_CONFIG_PATH=".config.th7"

spi = spidev.SpiDev()  # spi instance to read 12 bit ADC
spi_tc77 = spidev.SpiDev() # spi instance to read TC77 digital temperature chip
vref =1.0
vadj=1.0
pcb_temp=25.0
first_run=0

channels = [0,0,0,0,0,0,0,0]
class Thermocouple_Channel:

    def __init__(self, channel, filter_level=0, thermocouple_type="uv", offset=0.0, gain=106.2):

        self.channel = channel
        self.filter_level = filter_level
        self.thermocouple_type = thermocouple_type
        self.offset = offset
        self.value_uv = 0.0
        self.gain = gain
        self.value_c = -300.0


# references/pointers to thermocouple_channel objects are stored here
thermocouples = np.array([0, 0, 0, 0, 0, 0, 0], dtype=object)

# initialise array/list with 7 "blanks"
for i in range(0, 7):
    # filter level = -1 indicates the channel is `blank'
    thermocouples[i] = Thermocouple_Channel(i+1, 2, "K", 0, 106.8)



# Here, define each thermocouple channel connected to the TH7/ in use.
# 1st parameter is the No. of the channel; on PCB,
# 2nd is the filtering level, [0..3] (higher is harder filtering)
# 3rd is the T/C type as 1 upper-case character;
# currently supporting types: K, T, J, N, E, B, S


# channel, filter level, type, offset (in oC), gain (default 106)


thermocouples[0] = Thermocouple_Channel(1, 2, "K", -0.0, 106.8)
thermocouples[1] = Thermocouple_Channel(2, 2, "K", -0.0, 106.8)
thermocouples[2] = Thermocouple_Channel(3, 3, "K", -0.0, 106.8)
thermocouples[3] = Thermocouple_Channel(4, 3, "K", -0.0, 106.8)
thermocouples[4] = Thermocouple_Channel(5, 3, "K", -0.0, 106.8)
thermocouples[5] = Thermocouple_Channel(6, 3, "K", -0.0, 106.8)
thermocouples[6] = Thermocouple_Channel(7, 2, "K", -0.0, 106.8)



class ThermocoupleSetup:
     
    def __init__(self, root):
        self.root = root
        self.root.title("SDS Thermocouple Channel Setup")

        # Default values for gain and offset
        self.gain_value = 106.8
        self.offset_value = 0.0

        # Thermocouple Types
        self.tc_types = ["K", "J", "N", "T", "E", "B", "R", "S", "uv"]

        # Create UI elements
        self.create_widgets()

        # read in defaults file if exists
        self.load_setup_startup()
        # In the __init__ method, add:
        self.idle_interval = 500  # Idle time in milliseconds (5 seconds)
        self.root.after(self.idle_interval, self.on_idle)


    # Define the on_idle method:
    def on_idle(self):
        global first_run
        # print("The application is idle. Performing idle tasks...")
        current_temperature()
        calc_vref()
        
        for v in thermocouples:
            read_channel(v)
        if first_run == 0:
            first_run = 1
            #self.channel_widgets[0]["value_label"].config(text     =  "99.9")
            #self.channel_widgets[0]["value_label"].update()
        
        idx = 0
        for k in self.channel_widgets:
            if thermocouples[idx].thermocouple_type == "uv":
                k["value_label"].config(text=f'{thermocouples[idx].value_uv:.0f} uV')
                k["value_label"].update()
            elif thermocouples[idx].value_uv < -8000:
                k["value_label"].config(text="NOT CONNECTED")
                k["value_label"].update()
            else:
                k["value_label"].config(text=f'{thermocouples[idx].value_c:.2f}ºC')
                k["value_label"].update()
            idx += 1

        self.supply_widgets[0].config(text=f'Vcc {5.0/vadj:.2f}')
        self.supply_widgets[0].update()
        
        self.supply_widgets[1].config(text=f'Vadj {vadj:.2f}')
        self.supply_widgets[1].update()
        
        self.supply_widgets[2].config(text=f'PCB_T {pcb_temp:.2f}ºC')
        self.supply_widgets[2].update()
        self.root.after(self.idle_interval, self.on_idle)
        
    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="SDS:TH7 Thermocouple Channel Setup", font=("Arial", 14))
        header_label.grid(row=0, column=0, columnspan=4, pady=10)

        h1 = tk.Label(self.root, text="Channel", font=("Arial", 12))
        h1.grid(row=1, column=0, columnspan=1, pady=10)
        
        h2 = tk.Label(self.root, text="Type", font=("Arial", 12))
        h2.grid(row=1, column=1, columnspan=1, pady=10)
        
        h3 = tk.Label(self.root, text="Offset", font=("Arial", 12))
        h3.grid(row=1, column=2, columnspan=1, pady=10)
        
        h4 = tk.Label(self.root, text="Gain", font=("Arial", 12))
        h4.grid(row=1, column=3, columnspan=1, pady=10)
        
        h5 = tk.Label(self.root, text="Measurement", font=("Arial", 12))
        h5.grid(row=1, column=4, columnspan=1, pady=10)
        
        # Create the thermocouple channels (7 channels)
        self.channel_widgets = []
        for i in range(7):
            self.create_channel_widgets(i)

        # Submit Button to process the input
        self.submit_button = tk.Button(self.root, text="Apply", command=self.submit_setup)
        self.submit_button.grid(row=10, column=0, columnspan=1, pady=20)
        
        self.load_button = tk.Button(self.root, text="Load", command=self.load_setup)
        self.load_button.grid(row=10, column=1, columnspan=1, pady=20)
        
        self.save_button = tk.Button(self.root, text="Save", command=self.save_setup)
        self.save_button.grid(row=10, column=2, columnspan=1, pady=20)
        
        

        
        h6 = tk.Label(self.root, text="Vcc", font=("Arial", 12))
        h6.grid(row=9, column=0, columnspan=1, pady=10)
        
        h7 = tk.Label(self.root, text="Vadj", font=("Arial", 12))
        h7.grid(row=9, column=1, columnspan=1, pady=10)
        h8 = tk.Label(self.root, text="PCB_T", font=("Arial", 12))
        h8.grid(row=9, column=2, columnspan=2, pady=10)
        
        
        self.supply_widgets = []
        
        self.supply_widgets.append(h6)
        self.supply_widgets.append(h7)
        self.supply_widgets.append(h8)
        
    def create_channel_widgets(self, channel_number):
        # Create label for the channel
        channel_label = tk.Label(self.root, text=f"Channel {channel_number + 1}")
        channel_label.grid(row=channel_number + 2, column=0, padx=10, pady=5)

        # Create dropdown for thermocouple type
        tc_type_var = tk.StringVar(value=self.tc_types[0])  # Default to 'K'
        tc_type_menu = tk.OptionMenu(self.root, tc_type_var, *self.tc_types)
        tc_type_menu.grid(row=channel_number + 2, column=1, padx=10, pady=5)

        # Create entry for offset
        offset_var = tk.StringVar(value=str(self.offset_value))  # Default offset
        offset_entry = tk.Entry(self.root, textvariable=offset_var, width=7)
        offset_entry.grid(row=channel_number + 2, column=2, padx=10, pady=5)

        # Create entry for gain
        gain_var = tk.DoubleVar(value=self.gain_value)  # Default gain
        gain_entry = tk.Entry(self.root, textvariable=gain_var, width=7)
        gain_entry.grid(row=channel_number + 2, column=3, padx=10, pady=5)

        # Value field to display calculated temperature
        value_label = tk.Label(self.root, text="Value: Not Calculated", width=20)
        value_label.grid(row=channel_number + 2, column=4, padx=10, pady=5)

        # Store widgets in a list for future access
        self.channel_widgets.append({
            "tc_type": tc_type_var,
            "offset": offset_var,
            "gain": gain_var,
            "value_label": value_label,
            "gain_entry" : gain_entry,
            "offset_entry" : offset_entry,
            "tc_type_menu" : tc_type_menu

        })
        
        
        
    def load_setup(self):
        file_path = filedialog.askopenfilename(title='Load TH7 configuration', initialfile='.config.th7') # file_types[('config','*.th7')]
        self.activate_setup(file_path)

    def load_setup_startup(self):
        if os.path.exists(DEFAULT_CONFIG_PATH):
            self.activate_setup(DEFAULT_CONFIG_PATH)
        else:
            print("no config found")

    def activate_setup(self, file_path):
        with open(file_path, 'r') as file:
            config = json.load(file)
        channels =  config#config["channels"]
        for i, channel in enumerate(channels):
            print(f"Channel {i+1}: Type = {channel['type']} Gain = {channel['gain']}, Offset = {channel['offset']}")
            thermocouples[i] = Thermocouple_Channel(i+1, float(channel['filter']), channel['type'], float(channel['offset']), float(channel['gain'])) 
            #self.channel_widgets[i]['gain'] = channel['gain']
            #self.channel_widgets[i].config(gain=channel['gain'])
            #self.channel_widgets[i]['tc_type'] = channel['type']
            self.channel_widgets[i]['gain_entry'].delete(0,tk.END)
            self.channel_widgets[i]['gain_entry'].insert(0,channel['gain'])
            self.channel_widgets[i]['offset_entry'].delete(0,tk.END)
            self.channel_widgets[i]['offset_entry'].insert(0,channel['offset'])
            #
            self.channel_widgets[i]['tc_type'].set(channel['type'])
            self.channel_widgets[i].update()

    def save_setup(self):
        channels=[]
        for i, channel in enumerate(self.channel_widgets):
            channels.append({
                "type": channel["tc_type"].get(),
                "gain": channel["gain"].get(),
                "offset": channel["offset_entry"].get(),
                "filter": thermocouples[i].filter_level,
                })
        print(f'channels {channels}')

        file_path = filedialog.asksaveasfilename(title='Save as', initialfile='.config.th7', filetypes=[("TH7 Config", ".th7"),("All files", "*.*")], defaultextension=".th7")
        with open(file_path, 'w') as file:
            json.dump(channels, file, indent=4)

    def submit_setup(self):
        
        for i, channel in enumerate(self.channel_widgets):
            thermocouples[i].thermocouple_type = channel["tc_type"].get()
            thermocouples[i].gain =float( channel["gain"].get())
            thermocouples[i].offset = float(channel["offset_entry"].get())
            print(f'updated: type={channel["tc_type"].get()}, gain={float(channel["gain"].get())}, offset={float(channel["offset_entry"].get())}')


def init_spi():
    spi.open(0, 0)
    spi_tc77.open(0,1)
    spi.max_speed_hz =  10000
    spi_tc77.max_speed_hz =  10000

def current_temperature():
    global pcb_temp
    resp = spi_tc77.xfer2([0x00, 0x00, 0x00, 0x00]) # transfer four bytes
    number = resp[0] * 256 + resp[1]
          
    pcb_temp2 = (number/8.0) * 0.0625
    #print ("Temp: ", pcb_temp2, resp)
    pcb_temp = pcb_temp2

def calc_vref():
    global vadj
    global vref
    
    a = 0
    # prepare bits for ADC command to read channel
    cb1 = 4 + 2 + ((a & 4) >> 2)
    cb2 = (a & 3) << 6
    resp = spi.xfer2([cb1, cb2, 0x00])

    if a == 0:
        vref = resp[1] * 256.0 + resp[2] * 1.0
        vadj_now = vref/3355.4432
        vadj = vadj_now * 0.1 + vadj * 0.9
        #print ("vref: ", vref, "vadj: ", vadj)
        return

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

def read_channel(thermocouple):
    global vadj
    global vref
    global first_run
    
    a = thermocouple.channel
    # prepare bits for ADC command to read channel
    cb1 = 4 + 2 + ((a & 4) >> 2)
    cb2 = (a & 3) << 6
    resp = spi.xfer2([cb1, cb2, 0x00])

        # read into thermocouple channels + apply adjustment and "lag filters"
    if a >= 1 and a < 8:

            # this variable is not referenced anywhere else?
        ch1_adc12_5v = ((resp[1] * 256.0 + resp[2]*1.0) - vref) * vadj

        ch1 = resp[1] * 256.0 + resp[2]*1.0
        perfect = ((vref - ch1) * vadj)
        bigV = (perfect/4096.0)*5.0

            # the signal has been amplified G=101 so we need to multiply by 10,100.00
            #uv = bigV* 106 * 100
        uv = bigV * 100 * thermocouple.gain
        if first_run == 0:
            thermocouple.value_uv = uv
        else:
            if (abs(uv - thermocouple.value_uv) > 1000.0):
                thermocouple.value_uv = uv
            else:
                thermocouple.value_uv = apply_lag_filter(thermocouple.value_uv, uv, thermocouple.filter_level)

        tc_type = thermocouple.thermocouple_type
        uv_with_pcb = thermocouple.value_uv + translate_celsius_to_uv(pcb_temp, tc_type)
        valuec = translate_uv_to_celsius(uv_with_pcb, tc_type)
        thermocouple.value_c = valuec + thermocouple.offset

        #print(f"Ch {a}, temperature: {valuec} oC, uv: {uv_with_pcb}")
        


# Create the main window and run the app
if __name__ == "__main__":
    init_spi()
    root = tk.Tk()  # Create a Tkinter root window
    app = ThermocoupleSetup(root)  # Create an instance of the ThermocoupleSetup class
    root.mainloop()  # Start the Tkinter event loop

