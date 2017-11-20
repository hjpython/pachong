#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.error
try:
    urllib.request.urlopen('http://blog.ccsdn.net')
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
