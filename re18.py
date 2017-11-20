#!/usr/bin/env python
# coding=utf-8
import re 
pattern = '\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*'
string = "<a href=http://www.baidu.com''>百度首页</a><br><a href=mailto:c-e+o@iqianyue.com.cn'>电子邮件</a>"
result = re.search(pattern,string)
print(result)
