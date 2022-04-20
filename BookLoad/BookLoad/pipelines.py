# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookloadPipeline:
    fp = None
    count = 1

    def open_spider(self, spider):
        print("开始爬虫")
        self.fp = open("./星门.txt", "w", encoding="utf-8")

    def process_item(self, item, spider):
        Chapter_name = item['Chapter_name']
        Chapter_content = item['Chapter_content']
        self.fp.write(Chapter_name + "\n" + Chapter_content + "\n")
        print(self.count)
        self.count += 1
        return item

    def close_spider(self, spider):
        print("结束爬虫")
        self.fp.close()