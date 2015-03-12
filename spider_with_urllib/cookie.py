#encoding=utf-8

import urllib
import cookielib, urllib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
request = urllib2.Request(
    url = 'http://blog.csdn.net/u012150179/article/details/11749017', 
    headers = headers
)
#response = opener.open(request)
response = urllib2.urlopen(request)
print response.read()
