#coding: utf-8

from urlparse import urlparse
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.http import Request,FormRequest
from zhihu.items import *
from misc.log import *
from zhihu.settings import *
'''
1. 默认取sel.css()[0]，如否则需要'__unique':false
2. 默认字典均为css解析，如否则需要'__use':'dump'表明是用于dump数据
'''

class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["zhihu.com"]
    #URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。 因此，第一个被获取到的页面的URL将是该列表之一。 后续的URL将会从获取到的数据中提取。
    start_urls = ['http://www.zhihu.com/']
                

    rules = [
        #allow的值是正则表达式
        Rule(sle(allow=("/people/[^/]+/followees$"))),
        Rule(sle(allow=("/people/[^/]+/followers$",))),
        Rule(sle(allow=("/people/[^/]+$",)), callback = 'parse_item', follow = True),
        #Rule(sle(allow=("/people/[^/]+/about+$")), callback='parse_item', follow = False),
    ]
    
    def __init__(self, *a, **kwargs):
        super(ZhihuSpider, self).__init__(*a, **kwargs)

    def start_requests(self):
        return [FormRequest(
            "http://www.zhihu.com/login",
            formdata = {'email':'1191809906@qq.com',
                        'password':'rootroot123123'
            },
            callback = self.after_login
        )]

    def after_login(self, response):
        print '-------------login----------------'
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
    
    def parse_item(self, response):
        print response
        item = ZhihuPeopleItem()
        item['name'] = response.xpath('.//*[@id="zh-pm-page-wrap"]/div[1]/div[1]/div[1]/div/span[1]/text()').extract()
        item['location'] = response.xpath('.//*[@id="zh-pm-page-wrap"]/div[1]/div[1]/div[2]/div[2]/div/div/div/span[1]/span[1]/text()').extract() 
        item['business'] = response.xpath('.//*[@id="zh-pm-page-wrap"]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/span[1]/span[2]/a/text()').extract()
        print item['name']
        yield item

