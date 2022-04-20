# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class StPipeline:
    # def process_item(self, item, spider):
    #     #     return item


    def __init__(self):
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open('Sp.csv','w',encoding='utf-8',newline='')
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.file_name = ['title', 'videoLink']
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.file_name)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()
    #
    # def open_spider(self,spider):
    #     pass

    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        self.writer.writerow(dict(item))
        # 写入完返回
        return item

    def close_spider(self,spider):
        self.f.close()
