#!/usr/bin/python
# -*- coding:utf-8 -*-

# 编写的spider必须继承自scrapy的Spider类
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

from w3school.items import W3SchoolItem


class W3schoolSpider(Spider):
    """爬取w3school标签"""
    #log.start("log",loglevel='INFO')
    #spider的唯一名字，在不同的爬虫中需要定义不同的名字
    name = "w3school"
    allowed_domains = ["w3school.com.cn"]
    start_urls = [
        "http://www.w3school.com.cn/xml/xml_syntax.asp"
    ]
    # 爬虫的方法，调用时候传入从每一个URL传回的Response对象作为参数，response将会是parse方法的唯一的一个参数,
    # 这个方法负责解析返回的数据、匹配抓取的数据(解析为item)并跟踪更多的URL。
    def parse(self, response):
        # scrapy使用选择器Selector并通过XPath实现数据的提取
        sel = Selector(response)
        sites = sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        items = []
        base_url = get_base_url(response)

        for site in sites:
            item = W3SchoolItem()

            title = site.xpath('a/text()').extract()
            relative_url = site.xpath('a/@href').extract()[0]
            desc = site.xpath('a/@title').extract()

            item['title'] = title #[t.encode('utf-8') for t in title]
            item['link'] = urljoin_rfc(base_url, relative_url)
            item['desc'] = desc #[d.encode('utf-8') for d in desc]
            items.append(item)

            #记录
            log.msg("Appending item...",level='INFO')


        log.msg("Append done.",level='INFO')
        return items

