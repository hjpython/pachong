#!/usr/lin/python3.4
# coding=utf-8
import urllib.request
file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
#datalines = file.readlines()
dataline = file.readline()
#print(dataline)
#print(datalines)
fhandle = open('/home/hj/python/pythoncode/url/1.html','wb')
fhandle.write(data)
fhandle.close()
filename = urllib.request.urlretrieve('http://edu.51cto.com',filename = '/home/hj/python/pythoncode/url/2.html')
urllib.request.urlcleanup()
print(file.info())
print(file.getcode())
print(file.geturl())
