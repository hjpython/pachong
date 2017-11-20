#!/usr/bin/env python
# coding=utf-8
import re
string = 'hellomypythonhispythonourpythonend'
pattern = re.compile('.python.')
result = pattern.findall(string)
print(result)
