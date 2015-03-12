#!/usr/bin/python
#coding:UTF-8
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def strMatch(html):
    print html
    reg = r'(bitch)'
    strre = re.compile(reg)
    strlist = strre.search(html)
    if strlist:
        print 'yes, get the bitch\n'
    else:
        print 'sorry, the bitch is dead\n'

html = getHtml('http://bbs.seu.edu.cn')
strMatch(html)
