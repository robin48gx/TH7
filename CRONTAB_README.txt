

Edit crontab using the command "crontab -e"

Add this line

* * * * * /home/pi/projects/TH7/TH7_alive.sh

This crontab job will run every minute and make sure the TH7_logger
is running. If for some reason it is not running it will restart it.

You can view a crontab file with the command "crontab -l".
