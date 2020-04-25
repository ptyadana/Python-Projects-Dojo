import requests

response = requests.get(
    "https://api.exchangeratesapi.io/latest?symbols=USD")
print(response.text)
