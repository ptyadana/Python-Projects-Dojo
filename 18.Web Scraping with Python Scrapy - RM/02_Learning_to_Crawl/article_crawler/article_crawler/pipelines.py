# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
from datetime import datetime


class CheckItemPipeline:
    def process_item(self, article, spider):
        # check every required information is in the article or not
        if not article['title'] or article['url'] or article['last_edited']:
            raise DropItem('Missing information!')
        return article


class CleanDatePipeline:
    def process_item(self, article, spider):
        # parse last updated datetime info
        # This page was last edited on 24 February 2021, at 09: 11 (UTC).
        article['last_edited'] = article['last_edited'].replace(
            'This page was last edited on', '')
        article['last_edited'] = datetime.strptime(
            article['last_edited'], '%d %B %Y, at %H:%M')

        return article
