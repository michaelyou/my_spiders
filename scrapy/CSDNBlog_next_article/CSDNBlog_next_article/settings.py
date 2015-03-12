# -*- coding: utf-8 -*-

# Scrapy settings for CSDNBlog_next_article project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'CSDNBlog_next_article'

SPIDER_MODULES = ['CSDNBlog_next_article.spiders']
NEWSPIDER_MODULE = 'CSDNBlog_next_article.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CSDNBlog_next_article (+http://www.yourdomain.com)'

#禁止cookies，防止被ban
COOKIES_ENABLED = True

ITEM_PIPELINES = {
    'CSDNBlog_next_article.pipelines.CsdnblogNextArticlePipeline':300
    }
