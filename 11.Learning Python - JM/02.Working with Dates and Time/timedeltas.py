#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=35, seconds=12))

# print today's date
now = datetime.now()
print(now)

# print today's date one year from now
print("one year from now: ", str(now + timedelta(days = 365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks it will be : ", str(now + timedelta(days=2, weeks=2)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
one_week_ago = t.strftime("%A %B %d, %Y")
print("1 week ago, it was ", one_week_ago)


### How many days until April Fools' Day?
april_fool_day = datetime(year=2021, month=4, day=1)
no_of_days = april_fool_day - now
print(no_of_days)

today = date.today()
april_fool_day = date(year=today.year, month=4, day=1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if april_fool_day < today:
    print("April fool day already went by %d days ago" %((today - april_fool_day).days))
    april_fool_day = april_fool_day.replace(year = today.year + 1) #next year april fool day

# Now calculate the amount of time until April Fool's Day  
time_to_afd = april_fool_day - today
print(f"Next April fool days will be in {time_to_afd.days} days")

