#!/bin/sh

regex="^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
ip=$(curl -m 60 http://ipecho.net/plain | grep -P $regex)
if [ ! $ip ]; then
	ip=$(curl -m 60 http://echoip.com | grep -P $regex)
	if [ ! $ip ]; then
		ip=$(curl -m 60 http://myexternalip.com/raw | grep -P $regex)
		if [ ! $ip ]; then
			exit
		fi
	fi
fi

if [ $ip ]; then
	echo $ip > /tmp/pub-ip-$USER
fi