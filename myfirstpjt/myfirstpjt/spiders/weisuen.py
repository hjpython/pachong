# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem
class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    #allowed_domains = ['sina.com.cn']
    start_urls = ('http://slide.news.sina.com.cn/s/slide_1_2841_103185.html','http://slide.mil.news.sina.com.cn/k/slide_8_193_45192.html#p=1','http://news.sina.com.cn/pl/2016-09-12/doc-ifxvukhv8147404.shtml')
    def __init__(self,myurl=None,*args,**kwargs):
        super(WeisuenSpider,self).__init__(*args,**kwargs)
        myurllist = myurl.split('|')
        for i in myurllist:
            print('要爬取的网址为:%s'%i)
        self.start_urls = myurllist
    def parse(self, response):
        item = MyfirstpjtItem()
        item['urlname'] = response.xpath('/html/head/title/text()')
        print('以下将显示爬取的网址的标题')
        print(item['urlname'])
