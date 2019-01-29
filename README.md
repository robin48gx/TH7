# TH7
Code to read up to seven thermocouple inputs  from the raspberry pi using the SDS TH7 PCB

Enable spi in raspi-config.

Also, if you are running the pi as a user other than 'pi' add yourself to the spi group 
in /etc/group.

Clone the git hub repo here,

    $ git clone https://github.com/robin48gx/TH7.git 


change directory to TH7 and then run

    $ python ssh_terminal_TH7.py

The python file ssh_terminal_TH7.py is a simple terminal program
that displays the microvolts received from
the thermocouples and displays them in centigrade (for `k` type).
It also displays the PCB temperature and  the Vcc (voltage from USB to the pi;
the value is necessary for accurate calculation of microvolts).
It also creates a logging file (called 'TH7.log') showing the voltage supplied to the pi, the 
PCB temperature and the temperature of each connected thermocouple. This logs once per minute.
If logging is required run with nohup, i.e.

    $ nohup python ssh_terminal_TH7.py > /dev/null & 
    
The logging will then continue on the pi even if the terminal running it is closed.
The LEDs are controlled by the ssh_terminal_TH7.py program, so if they alternately blinking
this means the logging is continuing.
A script called 'plot_it.sh' will (using gnuplot) take data from the TH7.log file
and present it as a graph.

The python file thermometers_TH7.py adds to this with 
tkinter drawn thermometers. You may need the tkinter python 
modules for this : i.e. apt-get install python-tk.

Feel free to branch off this to make a temperature logger or a web interface.

For h/w 0.4 and above, an open thermocouple connection will display a very low 
micro-volts figure (typically < -7000) which is out of range for most thermocouples
and out of the range that most temperature readings would ever require (its below
abs zero for a k type for instance).
This means open thermocouples can be error flagged (as has been implemented for the
python `k` type thermocouple in this repo).
