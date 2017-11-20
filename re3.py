#!/usr/bin/env python
# coding=utf-8
import re
pattern = '\w\dpython\w'
string = 'abcdfphp345python_py'
result1 = re.search(pattern,string)
print(result1)
