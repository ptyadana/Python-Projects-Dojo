# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2020, 1, 31)
print(dt1)
print(isinstance(dt1, datetime))
print(dt1.timezone_name)

dt_us = pendulum.datetime(2022, 12, 15, tz="America/New_York")
print(dt_us)
print(isinstance(dt_us, datetime))
print(dt_us.timezone_name)


# TODO: convert the time to another time zone
d2 = dt1.in_timezone("Asia/Singapore")
print(d2)


# TODO: create a new datetime using the now() function
dt3 = pendulum.now()
print(dt3)


# TODO: Use the local function function
here = pendulum.local(2020, 12, 31)
print(here)
print(here.timezone.name)


# TODO: Use today, tomorrow, yesterday
today = pendulum.today()
tomorrow = pendulum.tomorrow()
yesterday = pendulum.yesterday("America/New_York")

print(today)
print(tomorrow)
print(yesterday)


# TODO: create a datetime from a system timestamp
t = time.time()
dt4 = pendulum.from_timestamp(t)
print(dt4)