# -*- coding: utf-8 -*-

# Scrapy settings for git_blog project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'git_blog'

SPIDER_MODULES = ['git_blog.spiders']
NEWSPIDER_MODULE = 'git_blog.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'git_blog (+http://www.yourdomain.com)'

#禁止cookies，防止被ban
COOKIES_ENABLED = True

ITEM_PIPELINES = {
    'git_blog.pipelines.GitBlogPipeline':300
    }