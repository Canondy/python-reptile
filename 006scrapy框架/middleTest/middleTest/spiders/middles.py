import scrapy


class MiddlesSpider(scrapy.Spider):
    name = 'middles'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text = response.text
        with open("./data/a.html", "w", encoding="utf-8") as fp:
            fp.write(page_text)

