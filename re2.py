#!/usr/bin/env python
# coding=utf-8
import re
pattern = '\n'
string = '''http://yum.iqianyue.com
http://baidu.com'''
result1 = re.search(pattern,string)
print(result1)
