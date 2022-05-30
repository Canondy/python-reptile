import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from zlsMovie.items import ZlsmovieItem

class ZlsSpider(CrawlSpider):
    name = 'zls'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://movie.douban.com/top250?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    # 打开数据库连接
    conn = Redis(host='127.0.0.1', port=6379)

    def parse_item(self, response):
        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        all_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in all_list:
            href = li.xpath('./div/div[1]/a/@href').extract()[0]
            # title = li.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
            ex = self.conn.sadd('movie_detail_url', href)
            # 利用redis中set去重功能，实现增量式爬虫
            if ex == 1:
                print("该url没有爬取过，可以进行数据爬取")
                item = ZlsmovieItem()
                # item["title"] = title
                item["href"] = href
                yield scrapy.Request(href, callback=self.parse_detail, meta={"item": item})
            else:
                print("该url爬取过，没有新数据爬取")

    def parse_detail(self, response):
        item = response.meta["item"]
        detail_title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]
        # content = response.xpath('//*[@id="link-report"]/span[1]/span//text()').extract()
        # content = ''.join(content)
        # print([detail_title, content])
        item['detail_title'] = detail_title
        # item['content'] = content
        yield item
