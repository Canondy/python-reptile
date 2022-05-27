# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# item类型的对象
class TestweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 添加用户名属性
    author = scrapy.Field()
    # 添加文案属性
    content = scrapy.Field()
    # pass
