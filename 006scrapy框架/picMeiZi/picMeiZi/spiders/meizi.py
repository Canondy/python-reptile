import scrapy


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    # allowed_domains = ['www.xxx.com']
    # 爬取的网址：https://www.pximg.com/meinv
    start_urls = ['https://www.pximg.com/meinv']

    # 生成通用的url模板  模板不可变
    url = 'https://www.pximg.com/meinv/page/%d'
    page_num = 2

    def parse(self, response):
        # 首先分析爬取结果中是否有想要的数据
        # 数据在HTML中，可以用xpath解析
        # 数据在异步返回的JSON中，用JSON()进行解析
        all_list = response.xpath('//*[@id="load-img"]/div[2]/ul/li')
        for item in all_list:
            # 图片 url地址  提取属性值元素
            pic_url = item.xpath("./a/img/@src").extract()
            # 图片标题
            title = item.xpath('./div/div[1]/p/a/text()').extract()
            print(title, pic_url)

        if self.page_num <= 4:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动发送请求
            # 参数url 就是新生成的new_url,   callback就是回调函数 专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
