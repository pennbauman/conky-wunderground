import urllib2
import json
import sys
import os

# Extract command line arguments and grab the wunderground API key
location = sys.argv[1]
nPeriods = int(sys.argv[2])
apiKey = open(os.getenv('HOME') + '/.api/wunderground','r').readline().split('\n')[0]

# Wunderground API call for 10 day forecast data
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/forecast10day/q/' + location + '.json')
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
forecast = parsed_json['forecast']['simpleforecast']['forecastday']

# Limit to nPeriods or the max days of forecast, whichever is lower
nPeriods = min(nPeriods,len(forecast))

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

# Iterate through nPeriods days starting from tomorrow and print their data
for i in range(nPeriods):
	date = int(forecast[i]['date']['day'])
	day = str(forecast[i]['date']['weekday_short'])[0:2]
	temp_low = int(forecast[i]['low']['fahrenheit'])
	temp_high = int(forecast[i]['high']['fahrenheit'])
	wind_avg = int(forecast[i]['avewind']['mph'])
	wind_avg_dir = int(forecast[i]['avewind']['degrees'])
	wind_max = int(forecast[i]['maxwind']['mph'])
	wind_max_dir = int(forecast[i]['maxwind']['degrees'])
	cond = icons[str(forecast[i]['icon'])]
	rain_chance = int(forecast[i]['pop'])
	humidity_avg = int(forecast[i]['avehumidity'])
	precipitation = str(forecast[i]['qpf_allday']['in'])
	print '{:2d} | {:3d} | {:2d} @ {:3d} | {:3d} | {:7s}\n{:2s} | {:3d} | {:2d} @ {:3d} | {:3d} | {:s}'.format(date,temp_low,wind_avg,wind_avg_dir,rain_chance,cond,day,temp_high,wind_max,wind_max_dir,humidity_avg,precipitation)
