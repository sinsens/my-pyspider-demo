#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-02-07 16:02:55
# Project: douban_demo

from pyspider.libs.base_handler import *
import re
import time
import random as rd    # 随机数



def dt(i):
    return time.time() + int(round(rd.random()*10,0)) + i  # 延迟时间

class Handler(BaseHandler):
    crawl_config = {
        #"proxy":'114.215.29.26:80',
    }
    
    @every(minutes=24 * 60 *5)
    def on_start(self):
        self.crawl('https://movie.douban.com/tag/', callback=self.index_page)
    
    # 标签列表，10小时爬一个标签
    def index_page(self, response):
        for each in response.doc('a[href^="https"]').items():
            if re.match("https://movie.douban.com/tag/\w+",each.attr.href,re.U):
                self.crawl(each.attr.href, callback=self.list_page,exetime=time.time()+10*60*60)
                
    # 爬标签
    def list_page(self, response):
        for each in response.doc('a[href^="https"]').items():
            # 电影详情
            if re.match("https://movie.douban.com/subject/\w+",each.attr.href,re.U):
                self.crawl(each.attr.href, callback=self.detail_page,exetime=dt(15))
                
        for each in response.doc('a[href^="https"]').items():  
            # 翻页
            if each.text() == u'后页>':
                self.crawl(each.attr.href, callback=self.list_page,exetime=dt(60*1.5))
                
    # 抓取结果
    def detail_page(self, response):
        actors = [x.text() for x in response.doc('a[rel="v:starring"]').items()]
        return {
            "影片名称": response.doc('span[property="v:itemreviewed"]').text(),
            "导演": [x.text() for x in response.doc('a[rel="v:directedBy"]').items()],
            "主演":actors,
            "上映日期": [t.text() for t in  response.doc('span[property="v:initialReleaseDate"]').items()],
            "片长": response.doc('span[property="v:runtime"]').text(),
            "评分": response.doc('strong[property="v:average"]').text()
        }
