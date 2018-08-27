import urllib2
import json
import sys
import os
import datetime

# Get time
now = datetime.datetime.now()
# Get zip code
zipCode = sys.argv[1]
# Get apiKey
apiKey = open(os.getenv('HOME') + '/.api/wunderground', 'r').readline().split('\n')[0]
# Get current weather data
urlFile = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/conditions/q/' + zipCode + '.json')
jsonString = urlFile.read()
urlFile.close()
jsonParsed = json.loads(jsonString)
weatherNow = jsonParsed['current_observation']
# Get 10 day forcast data
urlFile = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/forecast/q/' + zipCode + '.json')
jsonString = urlFile.read()
urlFile.close()
jsonParsed = json.loads(jsonString)
weatherForecast = jsonParsed['forecast']['simpleforecast']['forecastday']
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
# Assemble all relivant data
lines = [
	"Time: " + now.strftime("%Y-%m-%d %H:%M:%S%z"), #timestamp
	"Zip:  " + zipCode,
	"",
	str(weatherNow['temp_f']), # 0 current temp
	icons[str(weatherNow['icon'])], # 1 current cond
	
	str(weatherForecast[0]['low']['fahrenheit']), # 2 today's expected low temp
	str(weatherForecast[0]['high']['fahrenheit']), # 3 today's expected high temp
	icons[str(weatherForecast[0]['icon'])], # 4 today's expected cond
	str(weatherForecast[0]['pop']), # 5 today's expected rain chance (%)
	str(weatherForecast[0]['qpf_allday']['in']), # 6 today's expected rain fall (in.)

	str(weatherForecast[1]['low']['fahrenheit']), # 7 tomorrow's expected low temp
	str(weatherForecast[1]['high']['fahrenheit']), # 8 tomorrow's expected high temp
	icons[str(weatherForecast[1]['icon'])], # 9 tomorrow's expected cond
	str(weatherForecast[1]['pop']), # 10 tomorrow's expected rain chance (%)
	str(weatherForecast[1]['qpf_allday']['in']), # 11 tomorrow's expected rain fall (in.)	
]
saveText = ""
for line in lines:
	saveText = saveText + line + "\n"
# Write data to weather.txt
file = open(sys.path[0] + "/weather_save.txt", "w")
file.write(saveText)
file.close()
