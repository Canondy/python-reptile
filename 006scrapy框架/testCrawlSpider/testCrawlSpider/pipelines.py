# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TestcrawlspiderPipeline:
    def process_item(self, item, spider):
        # 现在有两个item，总么区分
        # 入库操作时，总么保证插入的数据一致性
        # 我这里可以判断title是否相等，  别的情况具体分析，有的是需求两个ID相等
        if item.__class__.__name__ == 'DetailItem':
            print(item['detail_title'], item['content'])
        else:
            print(item['title'], item['href'])
        return item
