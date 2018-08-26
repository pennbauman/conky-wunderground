import urllib2
import json
import sys
import os
import datetime

# Time
now = datetime.datetime.now()

# Extract command line arguments and grab the wunderground API key
location = sys.argv[1]
apiKey = open(os.getenv('HOME') + '/.api/wunderground', 'r').readline().split('\n')[0]

# Wunderground API call for current conditions data
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/conditions/q/' + location + '.json')
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
current = parsed_json['current_observation']

# Wunderground API call for 10 day forecast data
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/forecast10day/q/' + location + '.json')
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
forecast = parsed_json['forecast']['simpleforecast']['forecastday']

# Convert weather codes to readable
icons = {'chanceflurries' : 'Chance of Flurries',
	'chancerain' : 'Chance of Rain',
	'chancesleet' : 'Chance of Sleet',
	'chancesnow' : 'Chance of Snow',
	'chancetstorms' : 'Chance of Thunderstorms',
	
	'clear' : 'Clear',
	'cloudy' : 'Cloudy',
	'flurries' : 'Flurries',
	'fog' : 'Foggy',
	'hazy' : 'Hazy',
	'mostlycloudy' : 'Cloudy',
	'mostlysunny' : 'Sunny',
	'partlycloudy' : 'Partly Cloudy',
	'partlysunny' : 'Partly Sunny',
	'rain' : 'Raining',
	'sleet' : 'Sleeting',
	'snow' : 'Snowing',
	'sunny' : 'Sunny',
	'tstorms' : 'Thunderstorming',
	'unknown' : 'unknown'
}

cond = icons[str(current['icon'])]
cond = "%s%s" % (cond[0].upper(), cond[1:])

# Write data to weather.txt
file = open(sys.path[0] + "/weather_save.txt", "w")
lines = [
	now.strftime("%Y-%m-%d %H:%M"), #timestamp
	"",
	str(current['temp_f']), # 0 current temp
	cond, # 1 current cond
	str(forecast[0]['low']['fahrenheit']), # 2 today's expected low temp
	str(forecast[0]['high']['fahrenheit']), # 3 today's expected high temp
	icons[str(forecast[0]['icon'])], # 4 today's expected cond
	str(forecast[0]['pop']), # 5 today's expected rain chance (%)
	str(forecast[0]['qpf_allday']['in']), # 6 today's expected rain fall (in.)

	str(forecast[1]['low']['fahrenheit']), # 7 tomorrow's expected low temp
	str(forecast[1]['high']['fahrenheit']), # 8 tomorrow's expected high temp
	icons[str(forecast[1]['icon'])], # 9 tomorrow's expected cond
	str(forecast[1]['pop']), # 10 tomorrow's expected rain chance (%)
	str(forecast[1]['qpf_allday']['in']), # 11 tomorrow's expected rain fall (in.)	
]
text = ""
for line in lines:
	text = text + line + "\n"
file.write(text)
file.close()
