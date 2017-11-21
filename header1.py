#!/usr/bin/env python
# coding=utf-8
import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open('/home/hj/pachong/1.html','wb')
print(fhandle.write(data))
fhandle.close()
