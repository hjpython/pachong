#!/usr/bin/env python
# coding=utf-8
import re 
string1 = 'abpythonhellomypythonhispythonourpythonend'
string2 = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python.'
result1 = re.match(pattern,string1)
result2 = re.match(pattern,string2)
print(result1)
print(result2)
