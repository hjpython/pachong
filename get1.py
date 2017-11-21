#!/usr/bin/env python
# coding=utf-8
import urllib.request
keywd = 'hello'
url = 'http://www.baidu.com/s?wd='+keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandle = open('/home/hj/pachong/3.html','wb')
fhandle.write(data)
fhandle.close()
