import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()


time = datetime.time(23, 59, 59)
now = datetime.datetime.now()

# now = now.strftime("%H:%M:%S")

now = now.strftime("%H:%M:%S : %d-%m-%y")

print(date)
print(today)
print(time)
print(now)