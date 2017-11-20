#!/usr/bin/env python
# coding=utf-8
import urllib.request
key = '韦玮老师'
key_code = urllib.request.quote(key)
url = 'http://baidu.com/s?wd='
url_all = url + key_code
req = urllib.request.Request(url_all)
data = urllib.request.urlopen(req).read()
fhandle = open('/home/hj/python/pythoncode/url/3.html','wb')
fhandle.write(data)
fhandle.close()
