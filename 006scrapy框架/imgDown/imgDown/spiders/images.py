import scrapy
from imgDown.items import ImgdownItem

class ImgeasSpider(scrapy.Spider):
    name = 'images'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']


    # 文件没有下载成功。。。
    # 后面需要重新看看
    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 因为图片懒加载，所以使用标签伪属性
            img_url = div.xpath('./div/a/img/@src2').extract()[0]
            img_url = "https:" + img_url
            # print(img_url)
            # 把解析到的img_url放到item中
            item = ImgdownItem()
            item["img_url"] = img_url
            yield item
