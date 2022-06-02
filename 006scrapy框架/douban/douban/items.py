# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    is_sort = scrapy.Field()
    movie_cover_image_url = scrapy.Field()
    movie_detail_url = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    number = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    movie_type = scrapy.Field()
    desc = scrapy.Field()


class DetailItem(scrapy.Item):
    detail_title = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    starring = scrapy.Field()
    movie_length = scrapy.Field()
    introduction_title = scrapy.Field()
    movie_context = scrapy.Field()
