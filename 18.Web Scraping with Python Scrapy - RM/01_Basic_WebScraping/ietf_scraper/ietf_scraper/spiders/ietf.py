import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # title = response.css('span.title::text').get() # Approach 1) using css
        # title = response.xpath('//span[@class="title"]/text()') # Approach 2) using xpath
        # return {"title": title}

        info = {}

        # number
        number = response.xpath('//span[@class="rfc-no"]/text()').get()
        info['number'] = number

        # title
        title = response.xpath('//meta[@name="DC.Title"]/@content').get()
        info['title'] = title

        # date
        date = response.xpath('//span[@class="date"]/text()').get()
        info['date'] = date

        # description
        description = response.xpath(
            '//meta[@name="DC.Description.Abstract"]/@content').get()
        info['description'] = description

        # author
        author = response.xpath('//meta[@name="DC.Creator"]/@content').get()
        info['author'] = author

        # company
        company = response.xpath(
            '//span[@class="author-company"]/text()').get()
        info['company'] = company

        # address
        address = response.xpath('//span[@class="address"]/text()').get()
        info['address'] = address

        # text
        text = w3lib.html.remove_tags(
            response.xpath('//div[@class="text"]').get())
        info['text'] = text

        # headings
        headings = response.xpath(
            '//span[@class="subheading"]/text()').getall()
        info['headings'] = headings

        print(info)

        return info
