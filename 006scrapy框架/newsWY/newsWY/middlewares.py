# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse
import time

class NewswyDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 使用响应中间件，拦截各大板块响应对象，进行篡改
    # spider标识爬虫对象  爬虫文件
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest

        # 在爬虫类中（wangyi）获取浏览器对象
        bro = spider.bro
        # 挑选出指定的响应对象，进行篡改
        # 通过url找出request
        # 通过request找出调用的response
        if request.url in spider.url_list:
            bro.get(request.url)
            # 为了看效果 谁2秒
            time.sleep(2)
            # 拿到网页源码
            page_html = bro.page_source

            # 此响应对象是 各大板块 请求的url的响应结果
            # 针对这些response进行篡改
            # 实例化新的响应对象（动态加载出来的新闻数据）替换原来就的响应对象
            new_response = HtmlResponse(url=request.url, body=page_html, encoding="utf-8" , request=request)
            return new_response
        else:
            return response


        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

