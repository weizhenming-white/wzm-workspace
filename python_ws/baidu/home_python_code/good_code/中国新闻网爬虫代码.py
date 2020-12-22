#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

from lxml import etree


def getNewsURLList(baseURL):
    reponse = requests.get(baseURL)
    html = reponse.content.decode('gbk') 

    selector = etree.HTML(html)

    contents = selector.xpath('//div[@class="content_list"]/ul/li[div]')  # ????
    for eachlink in contents:
        url = eachlink.xpath('div/a/@href')[0]
        title = eachlink.xpath('div/a/text()')[0]
        ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
        yield title, url, ptime


def getNewsContent(urllist):
    for title, url, ptime in urllist:
        x = requests.get(url)
        html = x.content.decode('gbk')
        # html = x.content.decode()  #
        selector = etree.HTML(html)
        contents = selector.xpath('//div[@class="left_zw"]/p/text()')
        news = '\r\n'.join(contents)
        yield title, url, ptime, news


if __name__ == '__main__':
    urltemplate = 'http://www.chinanews.com/scroll-news/mil/{0}/{1}{2}/news.shtml'

    testurl = urltemplate.format('2017', '08', '29') 
    print(testurl)
    urllist = getNewsURLList(testurl)
    # for title,url,ptime in urllist:
    #     print title,url,ptime
    newscontens = getNewsContent(urllist)
    f = open('news.txt', 'wb+')  
    w = lambda x: f.write((x + u'\r\n').encode('utf-8'))
    for title, url, ptime, news in newscontens:
        w(u'~' * 100)
        w(title)
        w(url)
        w(ptime)
        w(news)
    f.close()
	


	
	
	
#------爬取某个时间范围内的军事新闻-------------------


#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
from lxml import etree


def getNewsURLList(baseURL):
    reponse = requests.get(baseURL)
    html = reponse.content.decode('gbk')
    # html = reponse.content.decode()

    selector = etree.HTML(html)

    contents = selector.xpath('//div[@class="content_list"]/ul/li[div]')  
    for eachlink in contents:
        url = eachlink.xpath('div/a/@href')[0]
        title = eachlink.xpath('div/a/text()')[0]
        ptime = eachlink.xpath('div[@class="dd_time"]/text()')[0]
        yield title, url, ptime


def getNewsContent(urllist):
    for title, url, ptime in urllist:
        x = requests.get(url)
        html = x.content.decode('gbk')
        # html = x.content.decode()  #
        selector = etree.HTML(html)
        contents = selector.xpath('//div[@class="left_zw"]/p/text()')
        news = '\r\n'.join(contents)
        yield title, url, ptime, news
		
import datetime
def getRange():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 8, 29)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        format_day=day.strftime('%Y/%m%d')
        yield format_day

if __name__ == '__main__':
    date_range=getRange();
    for date in date_range:
        urltemplate = 'http://www.chinanews.com/scroll-news/mil/{0}/news.shtml'
        testurl = urltemplate.format(date)
        print(testurl)
        urllist = getNewsURLList(testurl)

        newscontens = getNewsContent(urllist)
        f = open('news.txt', 'ab+')
        w = lambda x: f.write((x + u'\r\n').encode('utf-8'))
        for title, url, ptime, news in newscontens:
            w(u'~' * 100)
            w(title)
            w(url)
            w(ptime)
            w(news)
        f.close()














	