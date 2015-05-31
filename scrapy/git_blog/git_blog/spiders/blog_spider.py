
# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from git_blog.items import GitBlogItem
from scrapy.contrib.linkextractors import LinkExtractor


class Blog_article(CrawlSpider):

    """继承自CrawlSpider，实现自动爬取的爬虫。"""

    name = "blog"
    #设置下载延时
    #download_delay = 2
    allowed_domains = ['michaelyou.github.io']
    #第一篇文章地址
    start_urls = ['http://michaelyou.github.io/2015/05/30/PostgreSQL%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/']

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
        Rule(LinkExtractor(restrict_xpaths='//div[@class="post-nav-next post-nav-item"]/a'),
            callback='parse_item',
            follow=True,
            )
        ]

    def parse_item(self, response):

        #print "parse_item>>>>>>"
        item = GitBlogItem()
        sel = Selector(response)
        blog_url = str(response.url)
        #返回一个unicode字符串，为选中的数据
        blog_name = sel.xpath('//div[@class="post-header"]/h1/text()').extract()

        item['blog_name'] = [n.encode('utf-8') for n in blog_name]
        item['blog_url'] = blog_url.encode('utf-8')
        yield item

