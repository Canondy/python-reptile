import scrapy
from testWeibo.items import TestweiboItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # allowed_domains = ['www.weibo.com']
    # 首先分析爬取结果中的html中有么有想要的数据，看想要的数据是在html中，还是在异步请求结果的json字符串中
    # 如果html有可以用xpath方式提取
    # 如果html中没有想要的数据，看异步请求结果
    # 要抓取的是微博的url
    start_urls = ['https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=1&group_id=1028034288&containerid=102803_ctg1_4288_-_ctg1_4288&extparam=discover%7Cnew_feed&max_id=0&count=10']

    # 基于管道方式进行数据持久化操作
    def parse(self, response):
        # 1.响应结果取解析json字符串
        result = response.json()["statuses"]
        # 定义列表，用来存储解析后的数据
        actor_list = []
        # 循环取每一项，每个用户相对应的用户名和文案
        for item in result:
            # 取用户名
            author = item["user"]["screen_name"]
            # 取文案
            text = item["text_raw"].replace("\n", "").replace("​","")
            # 实例化item类型的对象
            item = TestweiboItem()
            # 将 author 和 text 封装到item中
            item["author"] = author
            item["content"] = text
            # 将item提交给管道
            yield item


# 基于终端指令进行数据持久化操作
"""
    def parse(self, response):
        # 1.响应结果取解析json字符串
        result = response.json()["statuses"]
        # 定义列表，用来存储解析后的数据
        actor_list = []
        # 循环取每一项，每个用户相对应的用户名和文案
        for item in result:
            # 取用户名
            author = item["user"]["screen_name"]
            # 取文案
            text = item["text_raw"].replace("\n", "").replace("​","")
            # print([author, text])
            # 把获取到的用户名和文案放到 字典中
            data = {
                "author": author,
                "content": text
            }
            # 然后把每一条数据放到列表里面
            actor_list.append(data)
        # 返回列表
        return actor_list
"""