import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem, DetailItem

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

            cont = ''.join(li.xpath("./div/div[2]/div[2]/p[1]//text()[2]").extract())
            cont = cont.replace("\n                        ", "").replace("\xa0", '')
            # 年份
            year = cont.split("/")[0].replace(" ", "")
            # 国家
            country = cont.split("/")[1]
            # 电影类型
            movie_type = cont.split("/")[2]
            # print(cont)
            # print([year, country, movie_type])
            item = DoubanItem()
            item['is_sort'] = is_sort
            item['movie_cover_image_url'] = movie_cover_image_url
            item['movie_detail_url'] = movie_detail_url
            item['movie_name'] = movie_name
            item['score'] = score
            item['number'] = number
            item['desc'] = desc
            item['year'] = year
            item['country'] = country
            item['movie_type'] = movie_type
            yield item


    # 解析详情页
    def parse_detail(self, response):
        # 排名
        is_sort = response.xpath('//*[@id="content"]/div[1]/span[1]/text()').extract()[0].split(".")[1]
        # 电影名称
        detail_title = response.xpath('//*[@id="content"]/h1/span/text()').extract()[0]
        # 导演
        director = ''.join(response.xpath('//*[@id="info"]/span[1]/span[2]//text()').extract())
        # 编剧
        screenwriter = ''.join(response.xpath('//*[@id="info"]/span[2]/span[2]//text()').extract())
        # 主演
        starring = ''.join(response.xpath('//*[@id="info"]/span[3]/span[2]//text()').extract())
        # 片长    缺少值，后续处理
        movie_length = ''.join(response.xpath('//*[@id="info"]/span[16]//text()').extract())
        # 简介标题
        introduction_title = ''.join(response.xpath('//*[@id="content"]/div[3]/div[1]/div[3]/h2/i/text()').extract())
        # 电影简介内容
        movie_context = ''.join(response.xpath('//*[@id="link-report"]/span[1]//text()').extract())
        movie_context = movie_context.replace("©豆瓣", "").replace(" ", "").replace("\n\u3000\u3000", "").replace("\n", "")
        # print([is_sort, movie_length])
        item = DetailItem()
        item['is_sort'] = is_sort
        item['detail_title'] = detail_title
        item['director'] = director
        item['screenwriter'] = screenwriter
        item['starring'] = starring
        # item['movie_length'] = movie_length
        item['introduction_title'] = introduction_title
        item['movie_context'] = movie_context
        yield item