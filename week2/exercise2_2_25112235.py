#Exercise 2.2. Practice using the Python interpreter as a calculator:
#1. The volume of a sphere with radius r is r³. What is the volume of a sphere with radius 5?
#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
#3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, 
# what time do I get home for breakfast?

import math
radius = 5
volume= 4/3 * math.pi * radius **3
print ('1.Volume:',volume)

book = 24.95
discount = 0.4
ship1 = 3
ship2 = 0.75
book_cost = book * (1 - discount) * 60
shipping_cost = ship1 + ship2 * 59
total = book_cost + shipping_cost
print('2.The total wholesale cost for 60 copies:', total)

easy_pace = 8 + 15/60
tempo = 7 + 12/60
total_time = 2 * easy_pace + 3 * tempo   # minutes
start_time = 6 * 60 + 52   # convert 6:52 AM into minutes
time_get_home = start_time + total_time
hour = int(time_get_home // 60)
minute = int(time_get_home % 60)
print('3.You get home at:', hour, ':', minute)
