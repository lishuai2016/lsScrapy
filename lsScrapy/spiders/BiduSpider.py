# -*- coding: utf-8 -*-
import scrapy


class BiduspiderSpider(scrapy.Spider):
    name = 'BiduSpider'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://http://www.baidu.com/']

    def parse(self, response):
        print(response.text)



