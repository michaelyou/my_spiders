import re
import json


from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.mail import MailSender


from hrtencent.items import *
from misc.log import *


class HrtencentSpider(CrawlSpider):
    mailer = MailSender()
    mailer.send(to = ["1191809906@qq.com"], subject = "scrapy", body = "welcome to scrapy")
    name = "hrtencent"
    allowed_domains = ["tencent.com"]
    download_delay = 0.1
    start_urls = [
        "http://hr.tencent.com/position.php",
    ]
    rules = [
        #Rule(sle(allow=("/position_detail.php\?id=\d*.*", )), callback='parse_job'),
        Rule(sle("/position.php\?&start=\d{,4}#a"), follow=True, callback='parse_job'),
    ]

    def parse_job(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        sites_even = sel.xpath('.//*[@id="position"]//tr[@class="even"]')
        print sites_even
        for site in sites_even:
            item = PositionDetailItem()
            item['sharetitle'] = site.xpath('td[@class="l square"]/a/text()').extract()
            item['location'] = site.xpath('td[4]/text()').extract()
            # item['duty'] = site.css('.c .l2::text').extract()
            relative_url = site.xpath('td[@class="l square"]/a/@href').extract()[0]
            item['link'] = urljoin_rfc(base_url, relative_url)
            items.append(item)
        info('parsed ' + str(response))
        return items
