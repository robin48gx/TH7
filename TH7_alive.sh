

a=`ps -ale | grep new_ssh_view.py`

if [ -z "$a" ]; then
	cd /home/pi/TH7_N;
	./new_ssh_view.py > /dev/null &
fi

