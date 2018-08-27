# Conky Wunderground

A set of scripts to get basic weather information on conky. 

Losely based on [conky_wunderground_scripts](https://github.com/iwvelando/conky_wunderground_scripts) by [iwvelando](https://github.com/iwvelando)

## Installation

Clone into ~/.conky/

	cd ~/.conky/
	git clone git@gitlab.com:pennbauman/conky-wunderground.git

Get an api key from [wunderground.com](https://www.wunderground.com/weather/api/) and put as the first and only line in ~/.api/wunderground 


## Usage

Somewhere in your conky before any other used of these scripts place, with your zip code in place of 00000:

	{execi 300 /usr/bin/env python2 ~/.conky/conky-wunderground/wunderground_weather_get.py 00000}


Each time you want to include weather in your conky use this code: 

	{execi 20 /usr/bin/env python2 ~/.conky/conky-wunderground/weather_file_read.py 0}

Replace 0 with the number of the data you want, numbers listed below:

	 0 => current temperature
	 1 => current condition
	 2 => today's expected low temperature
	 3 => today's expected high temperature
	 4 => today's expected condition
	 5 => today's expected rain chance (%)
	 6 => today's expected rain fall (in.)
	 7 => tomorrow's expected low temperature
	 8 => tomorrow's expected high temperature
	 9 => tomorrow's expected condition
	10 => tomorrow's expected rain chance (%)
	11 => tomorrow's expected rain fall (in.)	

An example version of this code in use in available in the EXAMPLE_CONKY.txt file. 

If you didn't install the scripts in ~/.conky/ change the paths to reflect the actually locations of the scripts. 
