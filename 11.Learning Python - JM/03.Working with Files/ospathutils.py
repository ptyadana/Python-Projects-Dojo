#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("Item exists: " + str(os.path.exists("test.txt")))
  print("Item is a file: " + str(os.path.isfile("test.txt")))
  print("Item is a directory: " + str(os.path.isdir("test.txt")))
  
  # Work with file paths
  print("Path of an item: " + str(os.path.realpath("test.txt")))
  print("Path and Item name: " + str(path.split(path.realpath("test.txt"))))

  # Get the modification time
  t = time.ctime(path.getmtime("test.txt"))
  print("Last modified time: " + str(t))

  # method 2
  print(datetime.datetime.fromtimestamp(os.path.getmtime("test.txt")))
  
  # Calculate how long ago the item was modified
  now = datetime.datetime.now()
  last_modified = datetime.datetime.fromtimestamp(os.path.getmtime("test.txt"))

  how_long_ago = now - last_modified
  print(f"Item was modifed {how_long_ago} ago..")
  print(f" Or {how_long_ago.total_seconds()} seconds ago..")

  
if __name__ == "__main__":
  main()
