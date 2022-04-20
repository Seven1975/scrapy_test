import scrapy
from BookLoad.items import BookloadItem

# 在笔趣阁中下载小说，只需要修改start_urls即可
# 修改为小说第一章网址，或者你想下载的起始章节网址
# 下载保存下来的小说名直接在pipelines.py中修改即可
class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.vipxs.la']
    start_url = "http://www.vipxs.la"
    # 其实页为星门小说第一章节网址为示例
    start_urls = ['https://www.vipxs.la/42_42168/11890905.html']

    def parse(self, response):
        Chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        Chapter_name = ''.join(Chapter_name.split())
        Chapter_content = response.xpath('//div[@id="content"]//text()').extract()
        Chapter_content = ''.join(Chapter_content)

        # 获取下一章节网址
        next_url = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract_first()
        # str处理
        next_url = self.start_url + str(next_url)
        # item类
        item = BookloadItem()
        item['Chapter_name'] = Chapter_name
        item['Chapter_content'] = Chapter_content.replace("\r", "")
        # 传递给管道
        yield item
        # 继续解析下一章节内容
        if next_url.find('html') != -1:
            yield scrapy.Request(next_url, callback=self.parse)

