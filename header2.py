#!/usr/bin/env python
# coding=utf-8
import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open('/home/hj/pachong/2.html','wb')
print(fhandle.write(data))
fhandle.close()

