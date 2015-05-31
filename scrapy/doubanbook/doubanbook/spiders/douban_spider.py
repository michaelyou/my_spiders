import re
import json

from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from doubanbook.items import *
from misc.log import *


class DoubanBookSpider(CrawlSpider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://book.douban.com/tag/"
    ]
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_book'),
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        Rule(sle(allow=("/tag/$", )), follow=True),
        Rule(sle(restrict_xpaths = ('.//*[@id="subject_list"]/div[2]/span[4]/a')))
    ]

    def parse_book(self, response):
        sel = Selector(response)
        item = DoubanSubjectItem()
        item['title'] = sel.xpath('.//*[@id="wrapper"]/h1/span/text()').extract()
        item['link'] = response.url
        item['content_intro'] = sel.xpath('.//*[@id="link-report"]/div[1]/div/p[1]/text()').extract()
        yield item

