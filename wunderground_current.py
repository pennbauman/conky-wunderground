import urllib2
import json
import sys
import os

# Extract command line arguments and grab the wunderground API key
location = sys.argv[1]
apiKey = open(os.getenv('HOME') + '/.api/wunderground', 'r').readline().split('\n')[0]

# Wunderground API call for current conditions data
f = urllib2.urlopen('http://api.wunderground.com/api/' + apiKey + '/conditions/q/' + location + '.json')
json_string = f.read()
f.close()
parsed_json = json.loads(json_string)
current = parsed_json['current_observation']

#Set a dictionary for parsing the icon field to a smaller text
icons = {
'chanceflurries': 'flurry?',
'chancerain': 'rain?',
'chancesleet': 'sleet?',
'chancesnow': 'snow?',
'chancetstorms': 'tstorm?',
'clear': 'clear',
'cloudy': 'cloudy',
'flurries': 'flurry',
'fog': 'fog',
'hazy': 'hazy',
'mostlycloudy': 'cloudy',
'mostlysunny': 'sunny',
'partlycloudy': 'cloudy~',
'partlysunny': 'sunny~',
'rain': 'rain',
'sleet': 'sleet',
'snow': 'snow',
'sunny': 'sunny',
'tstorms': 'tstorm',
'unknown': '???'
}

# Print current data
temp = str(current['temp_f'])
wspd = str(current['wind_mph'])
wgus = str(current['wind_gust_mph'])
wdir = str(current['wind_degrees'])
cond = icons[str(current['icon'])]
print '{:s} | {:s} ({:s}) @ {:s} | {:s}'.format(temp, wspd, wgus, wdir, cond)
