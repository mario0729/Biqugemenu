# -*- coding: utf-8 -*-
import scrapy
import requests
from Biqugemenu.items import bookinfoItem

class GetbiqugemenuSpider(scrapy.Spider):
    name = 'GetBiqugemenu'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/1_1000']

    def parse(self, response):
        item = bookinfoItem()
        a = response.css('#maininfo')
        item['bookname'] = a.css('h1::text').extract_first()
        item['author'] = a.css('p::text').extract_first().strip('作\xa0\xa0\xa0\xa0者：')
        item['bookintro'] = a.css('#intro p::text').extract_first()
        item['last_updatetime'] = a.css('p::text').extract()[4].strip('最后更新：')
        item['book_url'] = response.url
        print(a)
        print(item)
        yield item

        for i in range(1,3):
            for j in range(i*1000,i*1000+10):
                current_url = 'http://www.biquge.com.tw'+'/'+str(i)+'_'+str(j)
                print(current_url)
                if requests.get(current_url).status_code == 200:
                    yield scrapy.Request(url = current_url,callback=self.parse)
                else:
                    print('NO!')

