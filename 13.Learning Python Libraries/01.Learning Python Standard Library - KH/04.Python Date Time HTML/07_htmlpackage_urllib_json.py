# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import textwrap
import json


url = "https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224"
with urllib.request.urlopen(url) as f:
    text = f.read()
    decoded_text = text.decode("utf-8")
    print(textwrap.fill(decoded_text, width=100))
    
    # with open("data/book.json", "w") as file:
    #     file.write(decoded_text)
    
print()

json_obj = json.loads(decoded_text)
print(json_obj["kind"])
print(json_obj["items"][0]["searchInfo"]["textSnippet"])