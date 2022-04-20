# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksloadItem(scrapy.Item):
    book_Name = scrapy.Field()
    Chapter_content = scrapy.Field()
    Chapter_name = scrapy.Field()
