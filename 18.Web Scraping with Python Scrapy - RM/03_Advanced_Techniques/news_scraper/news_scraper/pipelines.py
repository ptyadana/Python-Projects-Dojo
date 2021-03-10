# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime


class NewsScraperPipeline:
    def process_item(self, item, spider):
        item.date = datetime.strptime(item.date.split('T')[0], '%Y-%B-%D')
        item.author = item.author.replace(', CNN', '')
        item.text = [text.strip() for text in item.text]
        return item
