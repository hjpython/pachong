#!/usr/bin/env python
# coding=utf-8
import re
pattern = 'yue'
string = 'http://yum.iqianyue.com'
result1 = re.search(pattern,string)
print(result1)
