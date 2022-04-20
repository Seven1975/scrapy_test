import scrapy
from st.items import StItem
import os
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

count = 1
class StspSpider(scrapy.Spider):

    name = 'stsp'
    allowed_domains = ['699pic.com']
    start_urls = ['https://699pic.com/video-sousuo-0-18-0-0-0-1-4-popular-0-0-0-0-0-0.html']


    def parse(self, response):
        global count
        count += 1
        print(response)
        # liList = response.xpath('//div[@class="video-list clearfix add-quick-recommend add-quick-recommend-b"]/ul/li')
                # print(liList)

        liList = response.xpath('//li')
        # liList = liList[12:]
        # liList = response.css('div')
        # print(len(liList))
        # print(liList)
        # print(response.text)
        # //div[@class='video-list clearfix add-quick-recommend add-quick-recommend-b quick-recommend-show']/ul/li/a[2]/h3/text()

        newfolderName = 'page{}'.format(count)
        # 步骤二 创建一个新的文件夹
        if not os.path.exists(newfolderName):
            os.mkdir(newfolderName)

        for li in liList[10:-6]:
            video_link = li.xpath("./a/div/video/@data-original").extract_first()
            videoLink = 'https:' + video_link
            title = li.xpath("./a[2]/h3/text()").extract_first()

            try:

                res = requests.get(videoLink,headers=headers)
                data = res.content
                # videopath = newfolderName + '/' + title
                try:
                    with open(newfolderName + '/' + title + '.mp4','wb') as f:
                        f.write(data)
                        print('%s下载成功'%title)
                except:
                    break
            except:
                break

            # print(videoLink,"--------",title)



            item = StItem(videoLink=videoLink,title=title)
            yield item

            if count == 40:
                break
        next_url = 'https://699pic.com/video-sousuo-0-18-0-0-0-{}-4-popular-0-0-0-0-0-0.html'.format(count)
        # next_href = response.xpath("//ul[@class='pagination cls fl']/li[last()]/a/@href").extract_first()
        # if next_href:
        #     next_url = response.urljoin(next_href)
        request = scrapy.Request(next_url)
        yield request