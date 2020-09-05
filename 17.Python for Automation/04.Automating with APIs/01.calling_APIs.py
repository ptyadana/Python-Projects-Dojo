import requests
import json


base_url = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {"upc": "883929609673"}

response = requests.get(base_url, params=parameters)

info = json.loads(response.content)
# print(type(info))
# print(info)
# print(json.dumps(info, indent=1))

items = info["items"]
item_info = items[0]
item_title = item_info["title"]
item_brand = item_info["brand"]
print(item_title, " by ",  item_brand)
