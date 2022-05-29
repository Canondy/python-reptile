import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunspiderSpider(CrawlSpider):
    name = 'sunSpider'
    # allowed_domains = ['www.xxx.com']
    # 这个网站加了腾讯反爬机制，我这IP可能被封了
    # start_urls = ['https://wz.sun0769.com/political/index/supervise?page=1']
    start_urls = ['https://movie.douban.com/top250?start=25']

    # 连接提取器：根据指定的规则 （allow = "正则表达式"）进行指定链接的提取
    link = LinkExtractor(allow=r'start=\d+')

    rules = (
        # 规则解析器：将链接提取器提取到的连接进行指定规则 （callback）的解析操作
        # follow=True 作用：可以将链接提取器继续作用到  连接提取器提取到的链接所对应的页面中
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
