
# frame work for a tkinter GUI 
# to control/configure a TH7
# on a raspberry pi

import tkinter as tk
from tkinter import messagebox

class ThermocoupleSetup:
    def __init__(self, root):
        self.root = root
        self.root.title("SDS Thermocouple Channel Setup")

        # Default values for gain and offset
        self.gain_value = 106.8
        self.offset_value = 0.0

        # Thermocouple Types
        self.tc_types = ["K", "J", "R", "T", "N", "NC"]

        # Create UI elements
        self.create_widgets()
        # In the __init__ method, add:
        self.idle_interval = 5000  # Idle time in milliseconds (5 seconds)
        self.root.after(self.idle_interval, self.on_idle)


    # Define the on_idle method:
    def on_idle(self):
        print("The application is idle. Performing idle tasks...")
        # Reschedule the idle callback
        self.root.after(self.idle_interval, self.on_idle)

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="Thermocouple Channel Setup", font=("Arial", 14))
        header_label.grid(row=0, column=0, columnspan=4, pady=10)

        # Create the thermocouple channels (7 channels)
        self.channel_widgets = []
        for i in range(7):
            self.create_channel_widgets(i)

        # Submit Button to process the input
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_setup)
        self.submit_button.grid(row=8, columnspan=4, pady=20)

    def create_channel_widgets(self, channel_number):
        # Create label for the channel
        channel_label = tk.Label(self.root, text=f"Channel {channel_number + 1}")
        channel_label.grid(row=channel_number + 1, column=0, padx=10, pady=5)

        # Create dropdown for thermocouple type
        tc_type_var = tk.StringVar(value=self.tc_types[0])  # Default to 'K'
        tc_type_menu = tk.OptionMenu(self.root, tc_type_var, *self.tc_types)
        tc_type_menu.grid(row=channel_number + 1, column=1, padx=10, pady=5)

        # Create entry for offset
        offset_var = tk.StringVar(value=str(self.offset_value))  # Default offset
        offset_entry = tk.Entry(self.root, textvariable=offset_var)
        offset_entry.grid(row=channel_number + 1, column=2, padx=10, pady=5)

        # Create entry for gain
        gain_var = tk.DoubleVar(value=self.gain_value)  # Default gain
        gain_entry = tk.Entry(self.root, textvariable=gain_var)
        gain_entry.grid(row=channel_number + 1, column=3, padx=10, pady=5)

        # Value field to display calculated temperature
        value_label = tk.Label(self.root, text="Value: Not Calculated", width=20)
        value_label.grid(row=channel_number + 1, column=4, padx=10, pady=5)

        # Store widgets in a list for future access
        self.channel_widgets.append({
            "tc_type": tc_type_var,
            "offset": offset_var,
            "gain": gain_var,
            "value_label": value_label
        })

    def submit_setup(self):
        # Iterate over each channel to retrieve the data
        for i, channel in enumerate(self.channel_widgets):
            tc_type = channel["tc_type"].get()
            offset = channel["offset"].get()
            gain = channel["gain"].get()

            try:
                offset = float(offset)
            except ValueError:
                messagebox.sho



# Create the main window and run the app
if __name__ == "__main__":
    root = tk.Tk()  # Create a Tkinter root window
    app = ThermocoupleSetup(root)  # Create an instance of the ThermocoupleSetup class
    root.mainloop()  # Start the Tkinter event loop

