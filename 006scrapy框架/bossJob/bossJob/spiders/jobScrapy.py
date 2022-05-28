import scrapy
from bossJob.items import BossjobItem

class JobscrapySpider(scrapy.Spider):
    name = 'jobScrapy'
    # allowed_domains = ['www.xxx.com']
    # boss
    # start_urls = ['https://www.lagou.com/wn/jobs?kd=iOS&city=北京']
    # start_urls = ['https://www.umei.cc/meinvtupian/xingganmeinv/']
    # 豆瓣电影top250
    start_urls = ['https://movie.douban.com/top250']

    # 实现分页爬取
    url = "https://movie.douban.com/top250?start=%d"
    start = 25
    def parse(self, response):
        # 返回解析后的页面源代码
        # print(response.body.decode())
        # 拿取所有的li
        all_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for item in all_list:
            # 电影名称
            title = ''.join(item.xpath("./div/div[2]/div[1]/a//text()").extract()).replace("\n                            ", "").replace(" ", "").replace("\n", "")
            # 导演
            director = ''.join(item.xpath("./div/div[2]/div[2]/p/text()").extract()).replace("\n                            ", "").replace("\xa0\xa0\xa0", " ").replace("\n", "")
            # 分数
            score = ''.join(item.xpath("./div/div[2]/div[2]/div/span[2]/text()").extract())
            # 人数
            number = ''.join(item.xpath("./div/div[2]/div[2]/div/span[4]/text()").extract()).replace("人评价", "")
            # 描述
            desc = ''.join(item.xpath("./div/div[2]/div[2]/p[2]/span/text()").extract())
            # 跳转链接
            target_url = item.xpath("./div/div[1]/a/@href").extract()[0]

            # 创建BossjobItem对象
            bossItem = BossjobItem()
            # 将解析出来的详情页url存放到item中
            bossItem["target_url"] = target_url

            # 拿到详情页面的url地址  请求详情页面
            # 手动发送清求
            # 请求传参： 通过meta={}, 可以将mete字典传递给请求对应的回调函数
            yield scrapy.Request(target_url, callback=self.parse_detail, meta={"item": bossItem})
            # print(target_url)
            # break

        # 进行分页爬取
        # self.start <= 225  因为一共250条数据，
        if self.start <= 50:
            new_url = format(self.url % self.start)
            self.start += 25
            yield scrapy.Request(new_url, callback=self.parse)


    def parse_detail(self, response):
        bossItem = response.meta["item"]
        detail_title = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]
        bossItem["detail_title"] = detail_title
        # print(detail_title)
        yield bossItem
