#!/usr/bin/env python
# coding=utf-8
import re
pattern1 = 'php|python'
pattern2 = 'python|php'
string = 'abcdpythonfphp345pythony_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)
