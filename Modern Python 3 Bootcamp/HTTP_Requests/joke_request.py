#Library Used: requests
#https://requests.readthedocs.io/en/master/

import requests

url = 'https://icanhazdadjoke.com'

# plain text
# response = requests.get(url, headers={'Accept':'text/plain'})

# JSON
response = requests.get(url, headers={'Accept':'application/json'})
data = response.json()
print(data['joke'])
