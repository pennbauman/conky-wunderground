#!/bin/bash

# Try and make sure the internet is connected
sleep 10

/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042 > /tmp/current-forecast-$USER &
curl -m 60 http://ipecho.net/plain -o /tmp/pub-ip-$USER &

sleep 10 && conky -dqc $HOME/.conkyrc_panel &

while true; do
	sleep 600
	/usr/bin/python2 $HOME/git/conky_wunderground_scripts/wunderground_current.py 77042 > /tmp/current-forecast-$USER &
	if [ ! -e /tmp/pub-ip-$USER ]; then
		curl -m 60 http://ipecho.net/plain -o /tmp/pub-ip-$USER &
	fi
done
