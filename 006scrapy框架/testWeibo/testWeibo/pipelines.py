# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TestweiboPipeline:
    fp = None
    # 重写父类方法： 该方法只调用一次，（创建文件操作）
    def open_spider(self, spider):
        print("start spider....")
        # 文件创建只进行一次
        self.fp = open("./data/weibo.csv", "w", encoding="utf-8")

    # 专门处理item类型的对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author = item["author"]
        content = item["content"]
        # 把item中的数据写到文件中
        self.fp.write(author + ":" + content + "\n")
        return item

    # 该方法只会在爬虫结束后调用一次
    def close_spider(self, spider):
        print("end spider...")
        # 关闭文件
        self.fp.close()
