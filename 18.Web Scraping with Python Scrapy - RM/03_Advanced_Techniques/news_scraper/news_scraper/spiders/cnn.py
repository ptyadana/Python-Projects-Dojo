import scrapy
from scrapy.spiders import CrawlSpider, SitemapSpider
from news_scraper.items import NewsArticle

# http://edition.cnn.com/robots.txt
# https://edition.cnn.com/sitemaps/cnn/index.xml
# https://www.cnn.com/sitemaps/article-2021-03.xml


class CnnSpider(SitemapSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    sitemap_urls = ['https://www.cnn.com/sitemaps/article-2020-10.xml']

    def parse(self, response):
        article = NewsArticle()
        # <script data-rh="true">
        article['url'] = response.url
        article['source'] = 'CNN'
        article['title'] = response.xpath('//h1/text()').get()
        article['description'] = response.xpath(
            '//meta[@name="description"]/@content').get()
        article['date'] = response.xpath(
            '//meta[@itemprop="datePublished"]/@content').get()
        article['author'] = response.xpath(
            '//meta[@itemprop="author"]/@content').get().replace(', CNN', '')
        article['text'] = response.xpath(
            '//section[@data-zone-label="bodyText"]/div[@class="l-container"]//*/text()').getall()
        return article
