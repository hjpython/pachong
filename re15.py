#!/usr/bin/env python
# coding=utf-8
import re 
string = 'hellomypythonhispythonourpythonend'
pattern = 'python.'
result1 = re.sub(pattern,'php',string)
result2 = re.sub(pattern,'php',string,2)
print(result1)
print(result2)
