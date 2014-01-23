# conky\_wunderground\_scripts

## Requirements

You'll need a Weather Underground API key; you can get a free one that offers more than enough daily calls to keep your forecast reasonably up to date.

[http://www.wunderground.com/weather/api/](http://www.wunderground.com/weather/api/)


## Install

Clone:

    git clone git://github.com/iwvelando/conky_wunderground_scripts.git

These scripts by default read your API key from a file in ~/.api/wunderground whose only text is the key; if you want to store it elsewhere or just supply it directly in the scripts you'll need to edit the line near the top that sets apiKey.

When run, these scripts just print the formatted output. To make use of it in conky you'll need to add the following lines to your .conkyrc where refresh\_interval is measured in seconds (I usually use 600, i.e. 10 minutes), and zipcode, number\_of\_hours, and number\_of\_days should be self-explanatory:

### Hourly Forecast
	execi refresh_interval /usr/bin/env python2 /path/to/wunderground_hourly_forecast.py zipcode number_of_hours

### Daily Forecast
	execi refresh_interval /usr/bin/env python2 /path/to/wunderground_daily_forecast.py zipcode number_of_days

### Current Conditions
	execi refresh_interval /usr/bin/env python2 /path/to/wunderground_current.py zipcode

Note that the path to /usr/bin/env may differ on your system; you can probably get away with "execi refresh_interval python2" though full paths are good practice. I haven't tested this with python 3.

### Runner Files
Included are shell scripts that I've used to implement these scripts on different machines; I'm not yet sure whether these should be kept separate and formalized. In any event they're currently very specific to my implementation and should be taken as a reference at best.

## Output Format

This was designed to provide a minimal text-based display of the weather rather than a bulkier but more informative option. The following explains the format of the output:

### Hourly Forecast
Hour | Temp | Wind Speed @ Wind Direction | Rain % | Condition

### Daily Forecast
Day (Number) | Min Temp | Average Wind Speed @ Wind Direction | Rain % | Condition

Day (Name) | Max Temp | Max Wind Speed @ Wind Direction | Humidity % | Precipitation

### Current Conditions
Temp | Wind Speed (Wind Gust Speed) @ Wind Direction | Condition

### Default Units
* Hour: 24-hour format
* Temp: degrees fahrenheit
* Wind Speed: miles per hour
* Wind Direction: the direction the wind comes from in degrees measured clockwise from north
* Precipitation: inches

### Condition Dictionary
The following maps the Weather Underground condition names to what's displayed:

* Chance of flurries: flurry?
* Chance of rain: rain?
* Chance of sleet: sleet?
* Chance of snow: snow?
* Chance of thunderstorms: tstorm?
* Clear: clear
* Cloudy: cloudy
* Flurries: flurry
* Fog: fog
* Hazy: hazy
* Mostly cloudy: cloudy
* Mostly sunny: sunny
* Partly cloudy: cloudy~
* Partly sunny: sunny~
* Rain: rain
* Sleet: sleet
* Snow: snow
* Sunny: sunny
* Thunderstorms: tstorm
* Unknown: ???

## Customizing Output

If you need to change the units or information displayed you can edit what is read from the API calls according to the documentation at:

[http://www.wunderground.com/weather/api/d/docs?d=index](http://www.wunderground.com/weather/api/d/docs?d=index)
