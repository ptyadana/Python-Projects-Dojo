# 
# Example file for parsing and processing JSON
# ref: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
#
import urllib.request 
import json


def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  print("\nNumber of events recorded : ", theJSON["metadata"]["count"])

  # for each event, print the place where it occurred
  for e in theJSON["features"]:
    print(e["properties"]["place"])

  # print the events that only have a magnitude greater than 4
  for e in theJSON["features"]:
    if e["properties"]["mag"] >= 4.0:
      print("%2.1f" %e["properties"]["mag"], e["properties"]["place"])
      
  # print only the events where at least 1 person reported feeling something
  print("Events that were felt: ")
  for e in theJSON["features"]:
    felt_reports = e["properties"]["felt"]

    if felt_reports != None:
      if felt_reports > 0:
        print("%2.1f" %e["properties"]["mag"], e["properties"]["place"], " reported ", str(felt_reports) + " times")
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))

  if webUrl.getcode() == 200:
    data = webUrl.read()
    printResults(data)
  else:
    print("received error!")
if __name__ == "__main__":
  main()
