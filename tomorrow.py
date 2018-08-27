import datetime

# Get todays weekday number
day_num = datetime.datetime.today().weekday()
day_num = day_num + 1

# Switch if past Sunday
if day_num == 7:
	day_num = 0

# Convert number to text
num_text = {
	0:"Monday", 
	1:"Tuesday", 
	2:"Wednesday", 
	3:"Thursday", 
	4:"Friday", 
	5:"Saturday", 
	6:"Sunday"
}
day_text = num_text[day_num]

# Output Day
print day_text