import sys

# Get data number
item = sys.argv[1]
item = int(item)
item += 2
# Read data from weather_save.txt
data = open(sys.path[0] + "/weather_save.txt", "r")
data = data.read().split('\n')[item]
# Print data
print(data)
