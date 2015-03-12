#!/usr/bin/python
#coding=utf-8
import re
import urllib
import urllib2
import collections
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

queue = collections.deque()
visited = set()

url = 'http://news.dbanotes.net/'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}
    print('已经抓取： ' + str(cnt) + '正在抓取<---- ' + url)
    cnt += 1
    try:
        urlop = urllib2.urlopen(url, timeout = 2)   #增加了超时
        if 'html' not in urlop.info().getheader('Content-Type'):
            continue
    except:
        continue

    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列---->' + x)
