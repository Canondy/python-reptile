# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class DoubanPipeline:

    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="127.0.0.1", port=3306, user="root", password="root123456", db="xo-music", charset="utf8")

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            if item.__class__.__name__ == "DoubanItem":
                # sql语句
                # self.cursor.execute('insert into movie values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (item['is_sort'], item['movie_cover_image_url'], item['movie_detail_url'], item['movie_name'], item['score'], item['number'], item['year'], item['country'], item['movie_type'], item['desc']))
                # self.conn.commit()
                pass
            else:
                # sql语句
                self.cursor.execute('insert into movie_detail values ("%s","%s","%s","%s","%s","%s")' % (item['detail_title'], item['director'], item['screenwriter'], item['starring'], item['introduction_title'], item['movie_context']))
                self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()