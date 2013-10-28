#!/bin/bash

# Try and make sure the internet is connected
sleep 10

/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042 > /tmp/current-forecast-$USER &
$HOME/git/conky_wunderground_scripts/pubip.sh &

while true; do
	sleep 600
	/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042 > /tmp/current-forecast-$USER &
	if [ ! -e /tmp/pub-ip-$USER ]; then
		$HOME/git/conky_wunderground_scripts/pubip.sh &
	fi
done
