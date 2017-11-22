#!/usr/bin/env python
# coding=utf-8
import urllib.request
import http.cookiejar
url = 'http://www.baidu.com/'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Encoding':'gb2312,utf-8','Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36','Connection':'keep-alive','referer':'baidu.com'}
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':'192.168.110.1:8888'})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key,value in headers.items():
    item = (key,value)
    headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open('/home/hj/pachong/12.html','wb')
fhandle.write(data)
fhandle.close()
