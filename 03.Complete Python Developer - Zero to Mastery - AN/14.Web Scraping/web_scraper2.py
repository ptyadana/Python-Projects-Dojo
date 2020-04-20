from bs4 import BeautifulSoup
import requests
import pprint

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

def scrap_the_page(page_number):
    base_url = 'https://news.ycombinator.com/news?p='+str(page_number)
    print(base_url)
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')

    links = soup.select('.storylink')
    sub_text = soup.select('.subtext')

    return create_custom_hacker_news(links, sub_text)

if __name__ == "__main__":
    custom_hn_lists = scrap_the_page(2)
    pprint.pprint(custom_hn_lists)


