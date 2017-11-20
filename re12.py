#!/usr/bin/env python
# coding=utf-8
import re 
string = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python.'
result1 = re.match(pattern,string)
result2 = re.match(pattern,string).span()
print(result1)
print(result2)
