# -*- coding: utf-8 -*-
import scrapy
import requests
from Biqugemenu.items import bookinfoItem

class GetbiqugemenuSpider(scrapy.Spider):
    name = 'GetBiqugemenu'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = []
    for i in range(1,20):
        for j in range(i*1000,i*1000+1000):
            url = 'http://www.biquge.com.tw'+'/'+str(i)+'_'+str(j)
            print(url)
            start_urls.append(url)

    def parse(self, response):
        item = bookinfoItem()
        a = response.css('#maininfo')
        item['bookname'] = a.css('h1::text').extract_first()
        item['author'] = a.css('p::text').extract_first().strip('作\xa0\xa0\xa0\xa0者：')
        item['bookintro'] = a.css('#intro p::text').extract_first()
        item['last_updatetime'] = a.css('p::text').extract()[4].strip('最后更新：')
        item['book_url'] = response.url
        print(item)
        yield item


    