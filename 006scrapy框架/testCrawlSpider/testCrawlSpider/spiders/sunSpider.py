import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from testCrawlSpider.items import TestcrawlspiderItem,DetailItem

class SunspiderSpider(CrawlSpider):
    name = 'sunSpider'
    # allowed_domains = ['www.xxx.com']
    # 这个网站加了腾讯反爬机制，我这IP可能被封了
    # start_urls = ['https://wz.sun0769.com/political/index/supervise?page=1']
    start_urls = ['https://movie.douban.com/top250?start=25']

    # 连接提取器：根据指定的规则 （allow = "正则表达式"）进行指定链接的提取
    link = LinkExtractor(allow=r'start=\d+')
    # 分析详情页url，得到以下的规则
    # https://movie.douban.com/subject/2129039/
    # https://movie.douban.com/subject/26387939/
    detail = LinkExtractor(allow=r'subject/\d+')

    rules = (
        # 规则解析器：将链接提取器提取到的连接进行指定规则 （callback）的解析操作
        # follow=True 作用：可以将链接提取器继续作用到  连接提取器提取到的链接所对应的页面中
        Rule(link, callback='parse_item', follow=True),
        Rule(detail, callback='parse_detail')
    )


    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        # print(response)
        all_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in all_list:
            href = li.xpath('./div/div[1]/a/@href').extract()[0]
            title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            # print(title, href)
            item = TestcrawlspiderItem()
            item['href'] = href
            item['title'] = title
            yield item


    def parse_detail(self, response):
        detail_title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]
        content = response.xpath('//*[@id="link-report"]/span[1]/span//text()').extract()
        content = ''.join(content)
        # print([detail_title, content])
        item = DetailItem()
        item['detail_title'] = detail_title
        item['content'] = content
        yield item