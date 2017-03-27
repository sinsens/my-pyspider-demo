#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-24 19:07:25
# Project: mm131

from pyspider.libs.base_handler import *
import urllib
from time import sleep
from time import time
import os


import random as rd
import re
import time

def get_proxy():
    proxy = ['106.14.61.27:3128','114.216.227.25:808','115.29.2.139:80','120.27.113.72:8888',
            '121.41.110.49:3128','123.206.93.108:8081','124.47.7.45:80','125.208.14.70:8090',
            '218.104.148.157:8080']
    i = rd.randint(0,len(proxy)-1)
    return proxy[i]

def get_UA():
    UserAgent_List = [
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    'Baiduspider','Googlebot','MSNBot','Baiduspider-image','YoudaoBot','Sogouwebspider','Sogouinstspider','Sogouspider2','Sogoublog',
    'SogouNewsSpider','SogouOrionspider','ChinasoSpider','Sosospider','yisouspider','EasouSpider']
    i = rd.randint(0,len(UserAgent_List)-1)
    ua = UserAgent_List[i]
    return ua

def dt(i=5):
    return time.time() + rd.randint(3,30) + i  # 延迟时间


class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.mm131.com/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.nav a').items():
            self.crawl(each.attr.href, callback=self.list_page,proxy = get_proxy(), headers={'User-Agent':get_UA()}, exetime=dt(60))

    def list_page(self, response):
             
        for each in response.doc('.main > .public-box img').items():
            self.crawl(each.attr.href, callback=self.pic_list, headers={'User-Agent':get_UA()}, exetime=dt(10), proxy = get_proxy())
            
        ''' 自循环 '''
        for each in response.doc('.page-en').items():
            self.crawl(each.attr.href, callback=self.list_page, headers={'User-Agent':get_UA()}, exetime=dt(60), proxy = get_proxy())

    def pic_list(self, response):
        typedir = response.url.split('/')[3]
        name = response.url.split('/')[4].split('_')[0].replace(".html","")
        title = response.doc('title').text().split('_')[0]
        ls = response.doc('.page-en').items()
        i = 0
        for item in ls:
            i += 1
        pics = []
        for i in range(0, i):
            url = 'http://img1.mm131.com/pic/' + name + '/' + str(i) + '.jpg'
            pics.append(url)

        save_data(typedir, title, name, pics)
        

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }


def save_data(typedir, title, name, picls):
    pass
    mydir = 'downloads/pic/' + typedir + '/' + name + '_' + title + '/'
    if os.path.exists(mydir) == False:
        os.makedirs(mydir)
    for i in picls:
        print '正在从', i, '获取图片'

        filename = mydir + urllib.unquote(i).decode('utf8').split('/')[-1]
        urllib.urlretrieve(i, filename)
        sleep(0.25)
        
    with open(mydir + title + '.txt', 'a') as f:
        f.write(title)
        f.write('\n')
        for data in picls:
            f.write(data + '\n')
                
    return {
        '美女分类': typedir,
        '标题': title,
        '名称/文件夹ID': name,
        '图片列表': picls
        }
