import requests
import lxml
from bs4 import BeautifulSoup


def scrape_page(url):
    print("\n scraping....", url)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
        count = 1

        for item in items:
            item_name = item.find("h4", class_="card-title").text.strip("\n")
            item_price = item.find("h5").text

            print("%s) Price: %s, Item Name: %s" %
                  (count, item_price, item_name))
            count += 1


def get_paginations_urls(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        # pagination numbers
        pages = soup.find("ul", class_='pagination')
        links = pages.find_all("a", class_="page-link")
        urls = []

        for link in links:
            page_number = int(link.text) if link.text.isdigit() else None
            if page_number != None:
                href = link.get("href")
                urls.append(href)

        return urls


if __name__ == "__main__":
    url = "https://scrapingclub.com/exercise/list_basic/"

    # scrape main page
    scrape_page(url + "?page=1")

    # get pagination numbers and its urls
    urls = get_paginations_urls(url)
    print(urls)

    # prepare full urls based on pagination url, and scrape the subsequence pages
    for link in urls:
        scrape_page(url + link)
