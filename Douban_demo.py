#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-02-07 16:02:55
# Project: douban_demo

from pyspider.libs.base_handler import *
import re
import time
import random as rd    # 随机数

def get_proxy():
    proxy=['39.82.126.45:9999',
           '61.157.198.66:8080','58.215.139.218:80','144.12.83.222:9999',
           '111.76.129.127:808',
           '27.209.202.36:9999',
           '219.145.244.250:3128',
           '120.76.79.24:80',
           '118.242.0.110:8909',
           '182.92.224.202:8088',
           '115.55.192.255:9999',
           '124.65.188.214:80',
           '220.248.230.217:3128',
           '49.74.86.186:9999',
           '211.20.254.76:80',
           '180.97.61.81:80',
           '106.46.136.85:808',
           '106.46.136.47:808',
           '60.205.184.144:3128',
           '183.128.241.62:808',
           '218.92.227.82:8080',
           '182.39.153.2:8118',
           '125.118.148.123:808',
           '211.151.158.159:80',
           '59.127.38.117:8080',
           '115.50.204.186:8118',
           '124.74.102.98:80',
           '59.46.64.50:80',
           '112.241.185.23:9999',
           '27.196.203.128:9999',
           '116.209.184.67:8000',
           '222.175.22.73:8998',
           '36.42.32.29:8080',
           '42.122.109.185:9999',
           '124.65.123.62:80',
           '118.244.179.220:80',
           '210.14.79.189:80',
           '118.99.36.15:808',
           '182.43.137.107:9999',
           '220.191.12.204:808',
           '106.46.136.11:808',
           '219.129.164.122:3128',
           '58.83.190.154:80',
           '27.207.144.33:9999',
           '27.215.172.87:8998',
           '113.121.7.48:9999',
           '218.92.220.15:8080',
           '223.199.146.146:9999',
           '118.178.227.171:80',
           '124.88.67.14:843',
           '202.111.31.26:80',
           '171.94.109.247:8998',
           '1.197.95.132:8998',
           '210.75.11.118:80',
           '113.5.80.93:8080',
           '182.38.201.220:9999',
           '210.22.108.90:80',
           '119.178.178.150:9999',
           '125.118.75.99:808',
           '118.123.245.163:3128',
           '210.242.249.205:8080',
           '218.4.179.34:80',
           '27.209.159.65:9999',
           '112.242.106.228:9999',
           '122.112.2.14:80',
           '112.246.207.105:9999',
           '118.123.22.192:3128',
           '183.203.167.45:8000',
           '112.252.53.10:9999',
           '27.220.172.27:9999',
           '39.70.78.59:9999',
           '112.253.19.159:8088',
           '218.106.154.149:80',
           '39.74.81.33:9999',
           '58.211.117.250:80',
           '101.201.115.179:3128',
           '123.169.117.218:9999',
           '101.200.46.171:80',
           '122.225.51.165:3128',
           '27.197.67.28:9999',
           '27.36.150.1:9999',
           '211.102.219.122:80',
           '106.46.136.27:808',
           '124.160.124.134:80',
           '111.1.3.34:8000',
           '58.211.142.2:80',
           '221.15.116.242:9999',
           '183.128.243.170:808',
           '58.58.32.134:80',
           '122.114.59.107:80',
           '218.56.132.156:8080',
           '218.92.145.33:8080',
           '210.22.180.94:80',
           '211.103.155.33:80',
           '183.141.149.81:3128',
           '60.220.197.7:8080',
           '110.182.29.70:9999',
           '111.76.133.15:808',
           '121.234.213.77:808',
           '121.226.202.96:8998']
    i = rd.randint(0,len(proxy)-1)
    ip = proxy[i]+''
    return ip

def get_header():
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
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
    i = rd.randint(0,len(UserAgent_List)-1)
    return UserAgent_List[i]

def dt(i):
    return time.time() + int(round(rd.random()*10,0)) + i  # 延迟时间

class Handler(BaseHandler):
    crawl_config = {
        'proxy': get_proxy(),
        'User-Agent': get_header()
    }
    
    @every(minutes=24 * 60 * 15)
    def on_start(self):
        print get_proxy(),get_header()
        self.crawl('https://movie.douban.com/tag/', callback=self.index_page)
    
    # 标签列表，1小时爬一个标签
    def index_page(self, response):
        print self.crawl_config['proxy']
        for each in response.doc('a[href^="https"]').items():
            if re.match("https://movie.douban.com/tag/\w+",each.attr.href,re.U):
                self.crawl(each.attr.href, callback=self.list_page,exetime=dt(60)+60*60,proxy=get_proxy(),headers= {'User-Agent': get_header()})
                
    # 爬标签
    def list_page(self, response):
        print self.crawl_config['proxy']
        for each in response.doc('a[href^="https"]').items():
            # 电影详情
            if re.match("https://movie.douban.com/subject/\w+",each.attr.href,re.U):
                self.crawl(each.attr.href, callback=self.detail_page,exetime=dt(30),proxy=get_proxy(),headers= {'User-Agent': get_header()})
                
        for each in response.doc('a[href^="https"]').items():  
            # 翻页
            if each.text() == u'后页>':
                self.crawl(each.attr.href, callback=self.list_page,exetime=dt(60*2),proxy=get_proxy(),headers= {'User-Agent': get_header()})
                
    # 抓取结果
    def detail_page(self, response):
        print self.crawl_config['proxy']
        actors = [x.text() for x in response.doc('a[rel="v:starring"]').items()]
        return {
            "影片名称": response.doc('span[property="v:itemreviewed"]').text(),
            "导演": [x.text() for x in response.doc('a[rel="v:directedBy"]').items()],
            "主演":actors,
            "上映日期": [t.text() for t in  response.doc('span[property="v:initialReleaseDate"]').items()],
            "片长": response.doc('span[property="v:runtime"]').text(),
            "评分": response.doc('strong[property="v:average"]').text()
        }
