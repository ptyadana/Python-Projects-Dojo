#create a script that let the user type in a search term and opens and search on the browser for that
# term on google

# Answer
# import requests

# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

# user_input = input('Enter anything that you would like to search: ')

# r = requests.get(f'https://www.google.com/search?q={user_input}',headers={'User-Agent':user_agent})

# print(r.status_code)

# Answer 2:

import webbrowser

query = input("Input your query: ")
webbrowser.open(f'https://www.google.com/search?q={query}')
# webbrowser.open("https://google.com/search?q=%s" % query)

# Explanation:
# We're using webbrowser  here which is a standard library that is used to open a web browser.
# First, we're getting the search term stored in variable query via the input  function. You need to first do a manual search on Google and observe how Google will construct the URL. Depending on where you are in the world the URL may be different, but the above URL should work everywhere.
# You will see that the URL contains your search term at the end. Therefore, we concatenate the first part of the URL with the search term we get from input .
