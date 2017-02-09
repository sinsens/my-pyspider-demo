#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-02-08 09:06:15
# Project: YunNan_stats

from pyspider.libs.base_handler import *
import re
import time

class Handler(BaseHandler):
    crawl_config = {
        
    }
    
    @every(minutes=30 * 24 * 60)
    def on_start(self):
        self.crawl('http://www.stats.yn.gov.cn/TJJMH_Model/newslist_tjsj.aspx?classid=133687', callback=self.index_page)

    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            # 30s抓一次
            if re.match('>>20',each.text()):
                print each.text(),' ',each.attr.href
                self.crawl(each.attr.href, callback=self.list_page,exetime=time.time()+1.5*60,retries=5)
            
    def list_page(self, response):
        for each in response.doc('a[class="index_right_style_1"]').items():
            print each.text(),' ',each.attr.href
            self.crawl(each.attr.href,callback=self.detail_page,retries=3,exetime=time.time()+15)
            
    @config(priority=2)
    def detail_page(self, response):
        data = response.doc('body > table:nth-child(2) > tbody > tr:nth-child(3) > td > table > tbody > tr > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table:nth-child(2) > tbody > tr:nth-child(2) > td > table > tbody').text()
        data+=response.doc('#eWebEditor_Temp_Excel_Sheet_Div > table > tbody').text()#2015+
        data+=response.doc('.nava > div').text()#2005年1月,2013? 2014?
        return {
            "title": response.doc('#lbTopic > b > font').text(),
            "data":data
        }
