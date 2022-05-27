# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 管道类中一个管道类对应将一组数据存储到一个平台或载体中


# 这个管道类是把接收到的item存放到本地 xxx.csv 文件中
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
        # 这个item就会传递给下一个即将被执行的管道类
        return item

    # 该方法只会在爬虫结束后调用一次
    def close_spider(self, spider):
        print("end spider...")
        # 关闭文件
        self.fp.close()


# 这个管道类是把接收到的item存放到数据库中
class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="root123456", db="xo-music", charset="utf8")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into py_scrapy values ("%s", "%s")'%(item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
