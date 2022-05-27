import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # allowed_domains = ['www.weibo.com']
    # 首先分析爬取结果中的html中有么有想要的数据，看想要的数据是在html中，还是在异步请求结果的json字符串中
    # 如果html有可以用xpath方式提取
    # 如果html中没有想要的数据，看异步请求结果
    # 要抓取的是微博的url
    start_urls = ['https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=1&group_id=1028034288&containerid=102803_ctg1_4288_-_ctg1_4288&extparam=discover%7Cnew_feed&max_id=0&count=10']

    def parse(self, response):
        # 1.响应结果取解析json字符串
        result = response.json()["statuses"]
        # 循环取每一项，每个用户相对应的用户名和文案
        for item in result:
            # 取用户名
            author = item["user"]["screen_name"]
            # 取文案
            text = item["text_raw"].replace("\n", "")
            print([author, text])
