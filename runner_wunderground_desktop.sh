#!/bin/bash

# Try and make sure the internet is connected
sleep 10

/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_daily_forecast.py 77070 7 > /tmp/daily-forecast-$USER &
/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_hourly_forecast.py 77070 17 > /tmp/hourly-forecast-$USER &
$HOME/git/conky_wunderground_scripts/pubip.sh &

sleep 10 && conky -dq &

while true; do
	sleep 600
	/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_daily_forecast.py 77070 7 > /tmp/daily-forecast-$USER &
	/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_hourly_forecast.py 77070 17 > /tmp/hourly-forecast-$USER &
	if [ ! -e /tmp/pub-ip-$USER ]; then
		$HOME/git/conky_wunderground_scripts/pubip.sh &
	fi
done
