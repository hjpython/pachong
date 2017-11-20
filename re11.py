#!/usr/bin/env python
# coding=utf-8
import re 
pattern1 = 'p.*y'  #贪婪模式
pattern2 = 'p.*?o' #懒惰模式
string = 'abcdfphp345pythony_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)
