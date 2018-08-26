import sys
import os

item = sys.argv[1]
item = int(item)
item += 2
#data = open(os.getenv('HOME') + "/.conky/wunderground_scripts/weather_save.txt", "r")
data = open(sys.path[0] + "/weather_save.txt", "r")
data = data.read().split('\n')[item]
#file.close()
print(data)
