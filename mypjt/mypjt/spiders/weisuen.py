# -*- coding: utf-8 -*-
import scrapy
from mypjt.items import MypjtItem

class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']
    start_urls = ('http://tech.sina.com.cn/d/s/2016-09-17/doc-ifxvyqwa3324638.shtml',)

    def parse(self, response):
        item = MypjtItem()
        item['title'] = response.xpath('/html/head/title/text()')
        print(item['title'])
        return item
