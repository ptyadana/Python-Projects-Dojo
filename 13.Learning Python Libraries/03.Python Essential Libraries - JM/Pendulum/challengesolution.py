# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
import pendulum

# Challenge: how many days until International Clash Day?
# https://www.kexp.org/internationalclashday/

# First, let's figure out what day today is
today = pendulum.today()
# Use the general format method to print the day and month
print("Today is: {0}".format(today.format("dddd, MMMM Do")))

# Next, create a date to represent International Clash Day
# Which, of course, is February 7
icd = pendulum.datetime(today.year, 2, 7)
# Use the general format method to print the day and month
print("Internation Clash Day is: {0}".format(icd.format("dddd, MMMM Do")))

# Figure out if the day has already gone by
if icd < today:
    old = today - icd
    print("International Clash Day went by {0} days ago".format(old.days))
    # if so, get the date for next year
    icd = icd.add(years=1)

# Now calculate the number of days until the next one
time_to_afd = icd - today
print("It's {0} days until Internation Clash Day!".format(time_to_afd.days))
