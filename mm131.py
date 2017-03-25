#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-24 19:07:25
# Project: mm131

from pyspider.libs.base_handler import *
import urllib
from time import sleep
from time import time
import os


class Handler(BaseHandler):
    _type = ''
    _title = ''
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.mm131.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.nav a').items():
            self.crawl(each.attr.href, callback=self.list_page)

    def list_page(self, response):
             
        for each in response.doc('.main > .public-box img').items():
            self.crawl(each.attr.href, callback=self.pic_list, exetime=time()+30)
            
        ''' 自循环 '''
        for each in response.doc('.page-en').items():
            self.crawl(each.attr.href, callback=self.list_page, exetime=time()+60*3)

    def pic_list(self, response):
        typedir = response.url.split('/')[3]
        print typedir
        name = response.url.split('/')[4].split('_')[0]
        self._title = response.doc('title').text()
        ls = response.doc('.page-en').items()
        i = 0
        for item in ls:
            i += 1
        pic = []
        for i in range(0, i):
            url = 'http://img1.mm131.com/pic/' + name + '/' + str(i) + '.jpg'
            pic.append(url)
            
        return ls, self._title,'dir:', typedir, 'id:', name, pic
        save_data(typedir, name, pic, response.doc('title').text())
        

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }


def save_data(typedir, name, ls, info):
    pass
    mydir = 'downloads/pic/' + typedir + '/' + name + '/'
    if os.path.exists(mydir) == False:
        os.makedirs(mydir)
    for i in ls:
        print '正在从', i, '获取图片'

        filename = mydir + urllib.unquote(i).decode('utf8').split('/')[-1]
        urllib.urlretrieve(i, filename)
        sleep(0.25)
        
    with open(mydir + 'info.txt', 'a') as f:
        f.write(info)
