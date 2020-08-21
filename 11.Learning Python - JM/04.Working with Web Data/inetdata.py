# 
# Example file for retrieving data from the internet
#

import urllib.request

def main():
  url = urllib.request.urlopen("https://www.google.com")
  print(f"Result: {url.getcode()}")

  data = url.read()
  print(data)

if __name__ == "__main__":
  main()
