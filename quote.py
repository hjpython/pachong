#!/usr/bin/env python
# coding=utf-8
import urllib.request
url = urllib.request.quote('http://www.sina.com.cn')
result = urllib.request.unquote(url)
print(result)
