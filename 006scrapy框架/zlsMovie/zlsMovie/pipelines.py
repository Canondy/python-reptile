# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ZlsmoviePipeline:
    def process_item(self, item, spider):
        conn = spider.conn
        item = str(item)
        conn.lpush("movie_detail", item)
        return item
