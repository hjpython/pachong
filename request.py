#!/usr/lin/python3.4
# coding=utf-8
import urllib.request
file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
dataline = file.readline()
fhandle = open('/home/hj/pachong/1.html','wb')
fhandle.write(data)
fhandle.close()

filename = urllib.request.urlretrieve('http://edu.51cto.com',filename = '/home/hj/pachong/2.html')
urllib.request.urlcleanup()
print(file.info())
print(file.getcode())
print(file.geturl())
