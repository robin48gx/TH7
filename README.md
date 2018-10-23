# TH7
Code to read up to seven thermocouple inputs  from the raspberry pi using the SDS TH7 PCB

Enable spi in raspi-config.

Also, if you are running the pi as a user other than 'pi' add yourself to the spi group 
in /etc/group.

Clone the git hub repo here,

    $ git clone https://github.com/robin48gx/TH7.git 


change directory to TH7 and then run

    $ python k_thermocouples_TH7.py

The python file ssh_terminal_TH7.py is a simple terminal program
that displays the microvolts received from
the thermocouples and displays them in centigrade (for K type).
It also displays the PCB temperature and  the Vcc (voltage from USB to the pi;
the value is necessary for accurate calculation of microvolts).

The python file thermometers_TH7.py adds to this with 
tkinter drawn thermometers.

Feel free to branch off this to make a temperature logger or a web interface.

For h/w 0.4 and above, an open thermocouple connection display a very low 
micro-volts figure (typically < -7000) which is out of range for most thermocouples
and out of the range that most temperature readings would ever require (its below
abs zero for a k type for instance).
This means open thermocouples can be error flagged (as has been implemented for the
python `k` type thermocouple in this repo).
