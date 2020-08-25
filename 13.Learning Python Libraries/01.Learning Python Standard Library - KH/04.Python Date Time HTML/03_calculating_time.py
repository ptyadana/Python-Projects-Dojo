# Calendar Module
from datetime import datetime, timedelta
import calendar


now = datetime.now()
test_date = now + timedelta(days= 2)
past_date = now - timedelta(weeks=3)

print(now)
print("2 days later: ", test_date.date())
print("3 weeks ago: ", past_date.date())

if test_date > past_date:
    print("comparing date time works.")

# Get Month of specific year
cal = calendar.month(2000, 1)
print(cal)

# get Weekday of specific year, month
cal2 = calendar.weekday(3000, 1, 1) #0:monday, 1: tuesday, etc
print(cal2)

# Is leap year or not
print(calendar.isleap(1999))
print(calendar.isleap(2000))