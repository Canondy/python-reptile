# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


# class ImgdownPipeline:
#     def process_item(self, item, spider):
#         return item

# ImagesPipeline专用于文件下载的管道，下载过程支持异步和多线程
class ImgsPipeline(ImagesPipeline):

    # 可以根据图片地址进行图片数据请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["img_url"])

    # 指定图片存储的路径
    # def file_path(self, request, response=None, info=None, *, item=None):
    #     img_name = request.url.split("/")[-1]
    #     return img_name

    def file_path(self, request, response=None, info=None):
        img_name = request.url.split("/")[-1]
        return img_name

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类
