import urllib2
import json
import sys
import os
import datetime

# Extract command line arguments and grab the wunderground API key
location = sys.argv[1]
nHours = int(sys.argv[2])
apiKey = open(os.getenv('HOME') + '/.api/wunderground','r').readline().split('\n')[0]

# Wunderground API call for astronomy data (for sunrise and sunset)
g = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/astronomy/q/' + location + '.json')
json_string = g.read()
g.close()
parsed_json = json.loads(json_string)
parsedSunrise = parsed_json['moon_phase']['sunrise']
parsedSunset = parsed_json['moon_phase']['sunset']

# Wunderground API call for hourly weather data
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/hourly/q/' + location + '.json')
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
hourly = parsed_json['hourly_forecast']
hours = len(hourly)
if nHours > hours:
	nHours = hours

# If sunrise or sunset hasn't happened yet, print them on the first line
now = datetime.datetime.today().replace(second=0,microsecond=0)
sunrise = now.replace(hour=int(parsedSunrise['hour']),minute=int(parsedSunrise['minute']))
sunset =  now.replace(hour=int(parsedSunset['hour']),minute=int(parsedSunset['minute']))
if sunrise > now:
	sun = 'Sunrise: ' + sunrise.strftime('%H:%M') + ', Sunset: ' + sunset.strftime('%H:%M')
	print sun
elif sunset > now:
	sun = 'Sunset: ' + sunset.strftime('%H:%M')
	print sun

#Set a dictionary for parsing the icon field to a smaller text
icons = {'chanceflurries' : 'flurry?',
	 'chancerain' : 'rain?',
	 'chancesleet' : 'sleet?',
	 'chancesnow' : 'snow?',
	 'chancetstorms' : 'tstorm?',
	 'clear' : 'clear',
	 'cloudy' : 'cloudy',
	 'flurries' : 'flurry',
	 'fog' : 'fog',
	 'hazy' : 'hazy',
	 'mostlycloudy' : 'cloudy',
	 'mostlysunny' : 'sunny',
	 'partlycloudy' : 'cloudy~',
	 'partlysunny' : 'sunny~',
	 'rain' : 'rain',
	 'sleet' : 'sleet',
	 'snow' : 'snow',
	 'sunny' : 'sunny',
	 'tstorms' : 'tstorm',
	 'unknown' : '???'}

# Iterate through nHours and print their data
for i in range(nHours):
	#hour = datetime.strptime(str(hourly[i]['FCTTIME']['civil']),"%I:%M %p").strftime("%I")
	hour = int(hourly[i]['FCTTIME']['hour'])
	#ampm = str(hourly[i]['FCTTIME']['ampm'])
	temp = int(hourly[i]['temp']['english'])
	cond = icons[str(hourly[i]['icon'])]
	wspd = int(hourly[i]['wspd']['english'])
	wdir = int(hourly[i]['wdir']['degrees'])
	rain_chance = int(hourly[i]['pop'])
	print '{:2d} | {:3d} | {:2d} @ {:3d} | {:3d} | {:7s}'.format(hour,temp,wspd,wdir,rain_chance,cond)
