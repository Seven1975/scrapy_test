# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksloadPipeline:

    def open_spider(self, spider):
        print("开始爬虫")

    def process_item(self, item, spider):
        book_name = item['book_Name']
        Chapter_name = item['Chapter_name']
        Chapter_content = item['Chapter_content']
        fp = open(book_name+'.txt', 'a+', encoding='utf-8')
        fp.write(Chapter_name + '\n'+ Chapter_content + '\n')
        fp.close()

    def close_spider(self,spider):
        print("结束爬虫")