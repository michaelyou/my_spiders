#!/usr/bin/python
#-*-coding:utf-8-*-

import time
from pprint import pprint
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from woaidu_crawler.items import WoaiduCrawlerItem
from woaidu_crawler.utils.select_result import list_first_item,strip_null,deduplication,clean_url

class WoaiduSpider(Spider):
    name = "woaidu"
    start_urls = (
            'http://www.woaidu.org/sitemap_1.html',
    )

    def parse(self,response):
        response_selector = Selector(response)
        next_link = list_first_item(response_selector.xpath(u'//div[@class="k2"]/div/a[text()="下一页"]/@href').extract())
        if next_link:
            next_link = clean_url(response.url,next_link,response.encoding)
            yield Request(url=next_link, callback=self.parse)

        for detail_link in response_selector.xpath(u'//div[contains(@class,"sousuolist")]/a/@href').extract():
            if detail_link:
                detail_link = clean_url(response.url,detail_link,response.encoding)
                yield Request(url=detail_link, callback=self.parse_detail)

    def parse_detail(self, response):
        woaidu_item = WoaiduCrawlerItem()

        response_selector = Selector(response)
        woaidu_item['book_name'] = list_first_item(response_selector.xpath('//div[@class="zizida"][1]/text()').extract())
        woaidu_item['author'] = [list_first_item(response_selector.xpath('//div[@class="xiaoxiao"][1]/text()').extract())[5:].strip(),]
        woaidu_item['book_description'] = list_first_item(response_selector.xpath('//div[@class="lili"][1]/text()').extract()).strip()
        woaidu_item['book_covor_image_url'] = list_first_item(response_selector.xpath('//div[@class="hong"][1]/img/@src').extract())

        download = []
        for i in response_selector.xpath('//div[contains(@class,"xiazai_xiao")]')[1:]:
            download_item = {}
            download_item['url'] = \
                strip_null( \
                    deduplication(\
                        [\
                            list_first_item(i.xpath('./div')[0].xpath('./a/@href').extract()),\
                            list_first_item(i.xpath('./div')[1].xpath('./a/@href').extract())\
                        ]\
                    )\
                )
            
            download_item['progress'] = list_first_item(i.xpath('./div')[2].xpath('./text()').extract())
            download_item['update_time'] = list_first_item(i.xpath('./div')[3].xpath('./text()').extract())
            download_item['source_site'] = \
                    [\
                        list_first_item(i.xpath('./div')[4].xpath('./a/text()').extract()),\
                        list_first_item(i.xpath('./div')[4].xpath('./a/@href').extract())\
                    ]\

            download.append(download_item)

        woaidu_item['book_download'] = download
        woaidu_item['original_url'] = response.url
        
        yield woaidu_item
