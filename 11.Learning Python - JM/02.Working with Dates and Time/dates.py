#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime 

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today date is ", today)

  # print out the date's individual components
  print("Date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today weekday number: ", today.weekday())
  
  days = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]
  print("Today weekday: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("Current Date and Time : ", today)

  # Get the current time
  time = datetime.time(datetime.now())
  print("Time: ", time)

  
if __name__ == "__main__":
  main();
  