import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name = 'first'
    # 允许的域名：用来限定start_urls列表中的哪些url可以进行发送请求
    # allowed_domains = ['www.xxxoo.com']
    # 起始url列表：  该列表中的url会被 scrapy 自动发送请求
    start_urls = ['http://www.baidu.com/', 'http://www.taobao.com/']

    # 用于数据解析：response参数表示的是请求成功后对应的响应结果
    # start_urls里面有几个url，就自动调用几次parse()方法，就有返回多少个响应结果
    def parse(self, response):
        print(response)
