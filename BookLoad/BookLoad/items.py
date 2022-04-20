# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookloadItem(scrapy.Item):
    Chapter_content = scrapy.Field()
    Chapter_name = scrapy.Field()
