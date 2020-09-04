import requests
import lxml
from bs4 import BeautifulSoup


url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    tags = soup.find_all("div", class_="quote")

    for index in range(len(quotes)):
        print(authors[index].text, " - ", quotes[index].text)
        quote_tags = tags[index].find_all("a", class_="tag")
        for t in quote_tags:
            print(t.text)
        print("")
