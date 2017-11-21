#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.parse
import http.cookiejar
url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LKlLD'
postdata = urllib.parse.urlencode({'username':'dyplm123','password':'dyp19931023'}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
fhandle = open('/home/hj/pachong/9.html','wb')
fhandle.write(data)
fhandle.close()
url2 = 'http://bbs.chinaunix.net/thread-4267193-1-1.html'
data2 = urllib.request.urlopen(url2).read()
fhandle = open('/home/hj/pachong/10.html','wb')
fhandle.write(data2)
fhandle.close()
