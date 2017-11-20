#!/usr/bin/env python
# coding=utf-8
import urllib.request
url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
file = urllib.request.urlopen(url)
data = file.read()
fhandle =  open('/home/hj/python/pythoncode/url/1.html','wb')
fhandle.write(data)
fhandle.close()
