from bs4 import BeautifulSoup
import requests
import pprint

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

base_url = 'https://news.ycombinator.com/news'
response = requests.get(base_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

with open('hacker_news.html', 'w') as file:
    file.write(soup.prettify())

links = soup.select('.storylink')
sub_text = soup.select('.subtext')

def sort_by_votes(hnlist):
    #sort by votes by descending order
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

def create_custom_hacker_news(links, sub_text):
    hn = []
    for index, item in enumerate(links):
        vote = sub_text[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().strip(' points'))
            if points > 150:
                title = links[index].getText()
                href = links[index].get('href', None)
                hn.append({'title':title,'href':href,'votes':points})
    return sort_by_votes(hn)

if __name__ == "__main__":
    custom_hn_lists = create_custom_hacker_news(links, sub_text)
    pprint.pprint(custom_hn_lists)

