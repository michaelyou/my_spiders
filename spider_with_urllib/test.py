#!/usr/bin/python
#coding:UTF-8
import re
import urllib
import urllib2

class HTTPCookieRedirectHandler(urllib2.HTTPRedirectHandler):
    __cookie_flag = 'Set-Cookie: '
        
    @staticmethod
    def __find_cookie(headers):
         print headers
         for msg in headers:
            if msg.find(HTTPCookieRedirectHandler.__cookie_flag) != -1:
                print HTTPCookieRedirectHandler.__cookie_flag
                return msg.replace(HTTPCookieRedirectHandler.__cookie_flag, '')
            return ''
 
    def http_error_301(self, req, fp, code, msg, httpmsg):
        cookie = HTTPCookieRedirectHandler.__find_cookie(httpmsg.headers)
        if cookie != '':
             req.add_header("Cookie", cookie)
        return urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, httpmsg)
 
    def http_error_302(self, req, fp, code, msg, httpmsg):
        cookie = HTTPCookieRedirectHandler.__find_cookie(httpmsg.headers)
        if cookie != '':
             req.add_header("Cookie", cookie)
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, httpmsg)

opener = urllib2.build_opener(HTTPCookieRedirectHandler)
try:
    #page = opener.open('http://blog.csdn.net/u012150179/article/details/11749017')
     page = opener.open('http://feeds.nytimes.com/click.phdo?i=8cd5af579b320b0bfd695ddcc344d96c')
except Exception, e:
    print e
html = page.read()
print html
