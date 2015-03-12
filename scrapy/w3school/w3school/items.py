# -*- coding: utf-8 -*-

# 所谓Item容器就是将在网页中获取的数据结构化保存的数据结构，类似于python中字典
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class W3SchoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
