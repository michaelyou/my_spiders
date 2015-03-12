#coding=utf-8
import gzip
import re
import cookielib
import urllib
import urllib2
from StringIO import StringIO
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = StringIO(data)   #解压方法与python3不同，注意注意
        data = gzip.GzipFile(fileobj=data).read()
        print('解压完毕!')
    except Exception, e:
        print e
        print('未经压缩, 无需解压')
    return data
                             
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
                                                              
def getOpener(head):
# deal with the Cookies
    cj = cookielib.CookieJar()
    pro = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
                                                                                                                
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}
                                                                                                                                              
url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)     # 解压
_xsrf = getXSRF(data.decode("utf-8"))
                                                                                                                                
url += 'login'
id = '1191809906@qq.com'
password = 'rootroot123'
postDict = {
    '_xsrf':_xsrf,
    'email': id,
    'password': password,
    'rememberme': 'y'
}

postData = urllib.urlencode(postDict).encode()
op = opener.open(url, postData)  #post请求
data = op.read()
data = ungzip(data)
                                                                                                                                                                             
print(data.decode())
