#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.parse
url = 'http://www.iqianyue.com/mypost/'
postdata = urllib.parse.urlencode({'name':'ceo@iqianyue.com','pass':'aA123456'}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open('/home/hj/python/pythoncode/url/5.html','wb')
fhandle.write(data)
fhandle.close()
