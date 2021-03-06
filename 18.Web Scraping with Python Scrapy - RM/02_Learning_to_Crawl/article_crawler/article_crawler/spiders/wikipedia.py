import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_crawler.items import Article

# class extends using CrawlSpider class


class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    # LinkExtractor actually parse the html, with regular expression we want to exclude pages with column :
    # follow = True means crawler will keep following innner links
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'),
                  callback='parse_info', follow=True)]

    # Custom settings for this specific crawler
    custom_settings = {
        'FEED_URI': 'articles.xml',
        'FEED_FORMAT': 'xml',
    }

    def parse_info(self, response):
        article = Article()

        article['title'] = response.xpath('//h1/text()').get()
        article['url'] = response.url
        article['last_edited'] = response.xpath(
            '//li[@id="footer-info-lastmod"]/text()').get()

        return article
