#!/usr/bin/env python
# coding=utf-8
import re
pattern = '\d{4}-\d{7}|\d{3}-\d{8}'
string = '021-6728263653682382265236'
result = re.search(pattern,string)
print(result)
