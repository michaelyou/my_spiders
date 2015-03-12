# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from CSDNBlog_next_article.items import CsdnblogNextArticleItem
from scrapy.contrib.linkextractors import LinkExtractor


class CSDNBlog_next_article(CrawlSpider):

    """继承自CrawlSpider，实现自动爬取的爬虫。"""

    name = "CSDNBlog_next_article"
    #设置下载延时
    #download_delay = 2
    allowed_domains = ['blog.csdn.net']
    #第一篇文章地址
    start_urls = ['http://blog.csdn.net/u012150179/article/details/11749017']

    #rules编写法一，官方文档方式
    #rules = [
    #    #提取“下一篇”的链接并**跟进**,若不使用restrict_xpaths参数限制，会将页面中所有
    #    #符合allow链接全部抓取
    #    Rule(LinkExtractor(allow=('/u012150179/article/details'),
    #                          restrict_xpaths=('//li[@class="next_article"]')),
    #         follow=True)
    #
    #    #提取“下一篇”链接并执行**处理**
    #    #Rule(LinkExtractor(allow=('/u012150179/article/details')),
    #    #     callback='parse_item',
    #    #     follow=False),
    #]

    #rules编写法二，更推荐的方式（自己测验，使用法一时经常出现爬到中间就finish情况，并且无错误码）
    
    
    #可用的xpaths   //li[@class="next_article"]
    rules = [
        Rule(LinkExtractor(allow=('/u012150179/article/details'),
                              restrict_xpaths=('.//*[@id="article_details"]/ul/li')),
             callback='parse_item',
             follow=True)
        ]

    def parse_item(self, response):

        #print "parse_item>>>>>>"
        item = CsdnblogNextArticleItem()
        sel = Selector(response)
        blog_url = str(response.url)
        #返回一个unicode字符串，为选中的数据
        blog_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()

        item['blog_name'] = [n.encode('utf-8') for n in blog_name]
        item['blog_url'] = blog_url.encode('utf-8')
        yield item

