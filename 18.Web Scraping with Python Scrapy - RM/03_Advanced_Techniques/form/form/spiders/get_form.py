import scrapy

# http://pythonscraping.com/linkedin/form.html


def generate_start_urls():
    names = ['Richard', 'Vivian', 'Ashley']
    quests = ['to learn scraping', 'to be awesome', 'to learn python']
    colors = ['red', 'green', 'blue']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=blue'.format(name, quest, color)
            for name in names for quest in quests for color in colors]


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
