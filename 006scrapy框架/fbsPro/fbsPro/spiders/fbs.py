import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from fbsPro.items import FbsproItem


class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://www.xxx.com/']
    redis_key = 'sun'

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        all_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in all_list:
            href = li.xpath('./div/div[1]/a/@href').extract()[0]
            title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            item = FbsproItem()
            item['href'] = href
            item['title'] = title
            yield item

    def make_requests_from_url(self, url):
        return scrapy.Request(url, dont_filter=True)