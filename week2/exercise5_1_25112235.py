import time

t = time.time()

days = t // 86400
remaining = t % 86400

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
seconds = remaining % 60

print(days,':', hours,':', minutes,':', seconds)
