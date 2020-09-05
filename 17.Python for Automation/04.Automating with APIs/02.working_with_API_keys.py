import requests
import json

base_url = "http://api.openweathermap.org/data/2.5/forecast"

APP_ID = "your_own_id"
parameters = {"appid": APP_ID, "q": "Singapore"}

response = requests.get(base_url, params=parameters)
print(json.dumps(json.loads(response.content), indent=1))
