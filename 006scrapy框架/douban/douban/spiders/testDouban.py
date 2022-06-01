import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestdoubanSpider(CrawlSpider):
    name = 'testDouban'
    # allowed_domains = ['www.xx.com']
    # 豆瓣电影top前250
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
        # top250首页的所有的li
        all_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in all_list:
            # 电影排序
            is_sort = li.xpath('./div/div[1]/em/text()').extract()[0]
            # 电影封面图片url地址
            movie_cover_image_url = li.xpath('./div/div[1]/a/img/@src').extract()[0]
            # 电影详情页url地址
            movie_detail_url = li.xpath('./div/div[1]/a/@href').extract()[0]
            # 电影名
            movie_name = li.xpath('./div/div[2]/div[1]/a/span/text()').extract()[0]
            # 分数
            score = ''.join(li.xpath("./div/div[2]/div[2]/div/span[2]/text()").extract())
            # 人数
            number = ''.join(li.xpath("./div/div[2]/div[2]/div/span[4]/text()").extract()).replace("人评价", "")
            # 描述
            desc = ''.join(li.xpath("./div/div[2]/div[2]/p[2]/span/text()").extract())
            # print(score, number, desc)
            # break

    #
    def parse_detail(self, response):
        # 电影名称
        detail_title = response.xpath('//*[@id="content"]/h1/span/text()').extract()[0]
        # 导演
        director = ''.join(response.xpath('//*[@id="info"]/span[1]/span[2]//text()').extract())
        # 编剧
        screenwriter = ''.join(response.xpath('//*[@id="info"]/span[2]/span[2]//text()').extract())
        # 主演
        starring = ''.join(response.xpath('//*[@id="info"]/span[3]/span[2]//text()').extract())
        # 电影类型 缺少值，后续处理
        movie_type = ''.join(response.xpath('//*[@id="info"]/span[5]/text()').extract())
        # 国家或地区  缺少值，后续处理
        country_region = response.xpath('//*[@id="info"]/text()[4]/text()').extract()
        # 上映时间  缺少值，后续处理
        release_time = ''.join(response.xpath('//*[@id="info"]/span[12]').extract())
        # 片长    缺少值，后续处理
        length = ''.join(response.xpath('//*[@id="info"]/span[16]//text()').extract())
        # 简介标题
        introduction_title = ''.join(response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/h2/i/text()').extract())
        # 电影简介内容
        movie_context = ''.join(response.xpath('//*[@id="link-report"]/span[1]//text()').extract())
        movie_context = movie_context.replace("©豆瓣", "").replace("\u3000", "").replace("\n", "")
        print([detail_title, movie_context])

