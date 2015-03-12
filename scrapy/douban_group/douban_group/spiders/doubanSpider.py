# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from douban_group.items import DoubanGroupItem
from scrapy.contrib.linkextractors import LinkExtractor

class doubanSpider(CrawlSpider):
    name = "douban"
    allowd_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/group/search?cat=1019&q=python",
    ]
    rules = [
        Rule(LinkExtractor(allow=('/group/[^/]+/$', )), callback='parse_group_home_page', process_request='add_cookie'),
        Rule(LinkExtractor(allow=('/group/explore\?tag', )), follow=True, process_request='add_cookie'),
        Rule(LinkExtractor(restrict_xpaths = ('//span[@class="next"]/a')), follow=True),
    ]
    
    def add_cookie(self, request):
        request.replace(cookies=[
            {'name': 'COOKIE_NAME','value': 'VALUE','domain': '.douban.com','path': '/'},
            ]);
        return request;
    
    def parse_group_home_page(self, response):
        self.log("Fetch group home page: %s" % response.url)
        sel = Selector(response)
        item = DoubanGroupItem()
        item['groupName'] = sel.xpath('.//*[@id="group-info"]/h1/text()').extract()
        yield item
