#!/usr/bin/env python
# coding=utf-8
import re
string = 'hellomypythonhispythonourpythonend'
pattern = '.python.'
result = re.compile(pattern).findall(string)
print(result)
