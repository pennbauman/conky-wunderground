#!/bin/bash

# Try and make sure the internet is connected
sleep 10

daily=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_daily_forecast.py 77070 7)
if [ $? == 0 ]; then
	echo $daily > /tmp/daily-forecast-$USER
fi
hourly=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_hourly_forecast.py 77070 17)
if [ $? == 0 ]; then
	echo $hourly > /tmp/hourly-forecast-$USER
fi
$HOME/git/conky_wunderground_scripts/pubip.sh &

sleep 10 && conky -dq &

while true; do
	sleep 600
	daily=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_daily_forecast.py 77070 7)
	if [ $? == 0 ]; then
		echo $daily > /tmp/daily-forecast-$USER
	fi
	hourly=$(/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_hourly_forecast.py 77070 17)
	if [ $? == 0 ]; then
		echo $hourly > /tmp/hourly-forecast-$USER
	fi
	if [ ! -e /tmp/pub-ip-$USER ]; then
		$HOME/git/conky_wunderground_scripts/pubip.sh &
	fi
done
