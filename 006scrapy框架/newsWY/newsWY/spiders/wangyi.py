import scrapy
from selenium import webdriver
from newsWY.items import NewswyItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    url_list = []

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path="/Users/liuhuan/PycharmProject/python-learn/test/venv/bin/chromedriver")

    def parse(self, response):
        # response.text 输出网页源代码
        # print(response.text)
        # 解析各个板块的url地址
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[2]/div[2]/div[2]/div[2]/div/ul')
        for li in li_list:
            # 国内url
            gn_url = li.xpath('./li[3]/a/@href').extract()[0]
            # 国际url
            gj_url = li.xpath('./li[4]/a/@href').extract()[0]
            # 军事url
            js_url = li.xpath('./li[6]/a/@href').extract()[0]
            # 航空
            air_url = li.xpath('./li[7]/a/@href').extract()[0]
            # print(gj_url, js_url, air_url)
            self.url_list = [gn_url, gj_url, js_url, air_url]
            # print(url_list)
        # 请求每一个模块中的url
        for url in self.url_list:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析每一个模块的标题和详情页的url
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            # 标题
            title = div.xpath('./div/div[1]/h3/a/text()').extract()
            # 详情url
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract()[0]
            # print(title, detail_url)

            item = NewswyItem()
            item['title'] = title

            # 对新闻详情页url发送请求
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

    # 对详情页内新闻内容的解析操作
    def parse_detail(self, response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content).replace(" ", "")
        item = response.meta["item"]
        item["content"] = content
        yield item

    # 关闭浏览器
    def closed(self, spider):
        self.bro.quit()
