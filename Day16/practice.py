from datetime import datetime

now = datetime.now();
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f'{day}/{month}/{year}, {hour}:{minute}, {timestamp}')

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)


date_string = "28 June, 2022"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

from datetime import date
today = date(year=2022, month=6, day=28)
new_year = date(year=2023, month=1, day=1)
time_left_for_newyear = new_year - today

print('Time left for new year: ', time_left_for_newyear)

today = date(year=2022, month=6, day=28)
then = date(year=1970, month=1, day=1)
diff = today - then
print(diff)

