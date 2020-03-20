#Library Used: requests
#https://requests.readthedocs.io/en/master/

import requests
import random

url = 'https://icanhazdadjoke.com/search'

print("---------------- Welcome to Dad Jokes ----------------")
search_string = input('Let me tell you a joke! Give me a topic:')

response = requests.get(
            url, 
            headers={'Accept':'application/json'},
            params={'term':search_string}
            )

data = response.json()
# print(data)
total_jokes = int(data['total_jokes'])

if total_jokes == 1:
    selected_joke = data['results'][0]['joke']
    print(f'I got 1 joke for you. Here is one.')
    print("\"" + selected_joke + "\"")
elif total_jokes > 1:
    r_num = random.randint(0,total_jokes)
    selected_joke = data['results'][r_num]['joke']
    print(f'I got {total_jokes} jokes for you. Here is one.')
    print("\"" + selected_joke + "\"")
else:
    print(f"Sorry I don't have any jokes about {search_string}. Please try again to enjoy more jokes.")