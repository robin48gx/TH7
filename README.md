# TH7
Code to read up to seven from thermocouple inputs  from the raspberry pi using the SDS TH7 PCB

Enable spi in raspi-config.

Also, if you are running the pi as a user other than 'pi' add yourself to the spi group 
in /etc/group.

change directory to TH7 and then run
$python k_thermocouples_TH7.py

This is a simple terminal program that displays the micro volts received from
the thermocouples and display them in centigrade (for K type).

Feel free to branch off this to make a temperature logger or a web interface.

Unused/disconnected channels display the PCB temperature.
