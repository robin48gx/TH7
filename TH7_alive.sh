

a=`ps -ale | grep TH7_logger.py`

if [ -z "$a" ]; then
	cd /home/pi/projects/TH7;
	./TH7_logger.py > /dev/null &
fi

