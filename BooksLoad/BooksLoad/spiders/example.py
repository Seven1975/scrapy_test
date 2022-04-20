
import scrapy
from BooksLoad.items import BooksloadItem
# 下载笔趣阁所有排行榜上前10的小说

class ExampleSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['www.vipxs.la']
    start_url = "http://www.vipxs.la"
    # 其实页为星门小说第一章节网址为示例
    start_urls = ['https://www.vipxs.la/paihangbang/']

    def parse(self, response):
        baihang_list = response.xpath('//*[@id="main"]/div')
        for baihang in baihang_list[2:]:
            bookurl_list = baihang .xpath('./ul[1]/li')
            for bookurl in bookurl_list[2:-1]:
                bookurl = bookurl.xpath('./a/@href').extract_first()
                yield scrapy.Request(bookurl, callback=self.parse_book)

    def parse_book(self, response):
        # 取出第一章节网址
        next_url = response.xpath('//*[@id="list"]/dl/dd[10]/a/@href').extract_first()
        yield scrapy.Request(self.start_url+str(next_url), callback=self.parse_chapter)

    def parse_chapter(self, response):
        book_Name = response.xpath('//div[@class="con_top"]/a[3]/text()').extract_first()
        book_Name = ''.join(book_Name.split())
        Chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        Chapter_name = ''.join(Chapter_name.split())
        Chapter_content = response.xpath('//div[@id="content"]//text()').extract()
        Chapter_content = ''.join(Chapter_content)

        # 获取下一章节网址
        next_url = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract_first()
        # str处理
        next_url = self.start_url + str(next_url)
        # item类
        item = BooksloadItem()
        item['book_Name'] = book_Name
        item['Chapter_name'] = Chapter_name
        item['Chapter_content'] = Chapter_content.replace("\r", "")
        # 传递给管道
        yield item
        # 继续解析下一章节内容
        if next_url.find('html') != -1:
            yield scrapy.Request(next_url, callback=self.parse_chapter)



