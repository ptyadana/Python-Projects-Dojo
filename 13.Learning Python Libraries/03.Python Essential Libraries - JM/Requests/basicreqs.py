# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# create a basic request for data
url = "http://httpbin.org/xml"
resp = requests.get(url)
print(resp.status_code)
print(resp.text)
print()

# create a request using parameters
args = {"key1": 1, "key2": "two", "key3": False}
resp = requests.get("http://httpbin.org/get", params=args)
print(resp.url)
print(resp.text)
print()

# create a request using POST
data = {"key": "value"}
resp = requests.post("http://httpbin.org/post", data=data)
print(resp.text)
print()

# create a request using custom headers
heads = {"my-custom-header": "This is custom header"}
resp = requests.get(url, headers=heads)
print(resp.text)