#!/usr/bin/env python
# coding=utf-8
import re 
pattern = '.python...'
string = 'abcdfphp345pythony_py'
result1 = re.search(pattern,string)
print(result1)
