#!/usr/bin/env python
# coding=utf-8
import re
string = 'hellomypythonhispythonourpythonend'
pattern = '.python.'
result1 = re.match(pattern,string)
result2 = re.search(pattern,string)
print(result1)
print(result2)
