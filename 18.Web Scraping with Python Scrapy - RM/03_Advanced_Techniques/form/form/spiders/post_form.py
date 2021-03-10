import scrapy
from scrapy.http import FormRequest

# http://pythonscraping.com/linkedin/form2.html


class GetFormSpider(scrapy.Spider):
    name = 'post_form'
    allowed_domains = ['pythonscraping.com']

    # "start_requests" is the method that scrapy looks for a list of form objects, just like "start_urls"
    def start_requests(self):
        names = ['Richard', 'Vivian', 'Ashley']
        quests = ['to learn scraping', 'to be awesome', 'to learn python']
        colors = ['red', 'green', 'blue']

        return [FormRequest('http://pythonscraping.com/linkedin/formAction2.php',
                            formdata={'name': name,
                                      'quest': quest, 'color': color},
                            callback=self.parse)
                for name in names for quest in quests for color in colors]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
