# -*- coding: utf-8 -*-
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 在pipelines.py中编写W3schoolPipeline实现对item的处理
# 在其中主要完成数据的查重、丢弃，验证item中数据，将得到的item数据保存等工作

class W3SchoolPipeline(object):
    def __init__(self):
        #模块codecs提供了一个open()方法，可以指定一个编码打开文件，使用这个方法打开的文件读取返回的将是unicode。
        #wb means write and in binary
        self.file = codecs.open('w3school_data_utf8.json', 'wb', encoding='utf-8')
    
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        print line
        # print line
        # 将得到的item实现解码，以便正常显示中文，最终保存到json文件中
        self.file.write(line.decode('unicode_escape'))
        return item
