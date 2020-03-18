#Web Scraping with BeautifulSoup
#https://beautiful-soup-4.readthedocs.io/en/latest/

import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://www.rithmschool.com/blog'
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text,'html.parser')
data = soup.find_all('article')

# print(data)

with open('blog_data.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    #write headers for csv file
    csv_writer.writerow(['title','url','datetime','content'])

    if len(data) > 0:
        for article in data:
            article_title = article.a.string
            article_url = article.a['href']
            article_date = article.time['datetime']
            article_content = article.p.contents[0]
            #write to csv file
            csv_writer.writerow([article_title,article_url,article_date,article_content])


