1.baidutieba.py包含的知识点
--将获取到的html文件中的一些没有进行的转义的的字符进行手工转义
--计算楼主发布的内容共有多少页
--将文件名中的一些不应该出现的字符全部替换、
--将收到的数据写入到本地文件中


2.qiubai_spider.py
--修改了headers，伪装成浏览器，使用urllib2.request使用新的header
--针对urllib2.request的错误处理


3.zhihu.py
--收到的回复数据时gzip压缩的，使用了ungzip对数据进行解压
--针对需要用户名，密码登陆的网址进行处理，处理cookie，新建opener


4.startup_news_spider.py
--将新抓取到的页面里面的链接放到一个queue里面，使用一个循环来循环抓取这些链接并放入新的链接


5.bfs_nthread_spider.py
--使用了sys.setdefaultencoding('utf8')
--多线程
--广度优先算法
--线程池和单个线程的创建
--将任务放到队列中去，如何放，如何取
--日志模块
--改了headers，使用urllib2.request使用新的header
--爬去返回html中的链接，并过滤无效链接
--解析命令行参数

6.douban_movie_spider2.py
--使用了beautifulsoup来解析html文件
--建立文件夹
--下载图片urllib.urlretrieve
--print输出字典和list的时候对中文只输出unicode编码，使用json来输出中文
--对列表中的元素进行排序

7.dytt8_movie_spider2.py
--使用了urllib2.build_opener()和opener.add_handler = headers


