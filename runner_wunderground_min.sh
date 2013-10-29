#!/bin/bash

# Try and make sure the internet is connected
sleep 10

weather=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042)
if [ $? == 0 ]; then
	echo $weather > /tmp/current-forecast-$USER
fi
$HOME/git/conky_wunderground_scripts/pubip.sh &

while true; do
	sleep 600
	weather=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042)
	if [ $? == 0 ]; then
		echo $weather > /tmp/current-forecast-$USER
	fi
	if [ ! -e /tmp/pub-ip-$USER ]; then
		$HOME/git/conky_wunderground_scripts/pubip.sh &
	fi
done
