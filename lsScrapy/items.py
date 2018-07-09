# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LsscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    #定义的字段名和下面pipeline中的要对应起来
    text = scrapy.Field()
    author = scrapy.Field()
    pass
