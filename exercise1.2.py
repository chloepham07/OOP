#Exercise 1.2. Start the Python interpreter and use it as a calculator.
#1. How many seconds are there in 42 minutes 42 seconds?
#2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
#3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
minutes = 42
seconds = 42
km = 10

total_seconds = minutes*60 + seconds
miles = km / 1.61

print('seconds:', total_seconds)
print('miles:', miles)

pace_minutes = (minutes + seconds/60) / miles
pace_seconds = (minutes*60 + seconds) / miles
print('pace:', pace_minutes, 'min/mile')

speed = miles / (minutes/60 + seconds/3600)
print('speed:', speed, 'mph')