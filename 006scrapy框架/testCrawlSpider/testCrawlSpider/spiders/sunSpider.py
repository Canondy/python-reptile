import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunspiderSpider(CrawlSpider):
    name = 'sunSpider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    # 连接提取器：根据指定的规则 （allow = "正则表达式"）进行指定链接的提取
    link = LinkExtractor(allow=r'Items/')

    rules = (
        # 规则解析器：将链接提取器提取到的连接进行指定规则 （callback）的解析操作
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
