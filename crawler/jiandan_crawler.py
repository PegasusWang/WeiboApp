#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler import Spider
import requests
from bs4 import BeautifulSoup
import traceback
import lxml
from StringIO import StringIO
import time


class JiandanSpider(Spider):

    def get_meizi(self, html):
        "http://jandan.net/ooxx/page-%#comments, from 900 to 1496"
        soup = BeautifulSoup(html, 'lxml')
        img_tag_list = soup.find_all('img')
        img_url_list = [i.get('src') for i in img_tag_list]
        return img_url_list

    def get_wuliao(self, html):
        "http://jandan.net/pic/page-%s#comments, from 4000 to 7058"
        return self.get_meizi(html)


def test_meizi():
    for i in range(900, 903):
        time.sleep(1)
        url = "http://jandan.net/ooxx/page-%s#comments" % str(i)
        print url
        s = JiandanSpider(url)
        html = s.get_html()
        img_list = s.get_meizi(html)
        for i in img_list:
            print i
            filename = i.rsplit('/')[-1]
            #with open(filename, 'wb') as f:
                #f.write(requests.get(i).content)


def test_wuliao():
    for i in range(4000, 4001):
        url = "http://jandan.net/pic/page-%s#comments" % str(i)
        print url
        s = JiandanSpider(url)
        html = s.get_html()
        img_list = s.get_wuliao(html)
        for i in img_list:
            filename = i.rsplit('/')[-1]
            print filename
            with open(filename, 'wb') as f:
                f.write(requests.get(i).content)


if __name__ == '__main__':
    test_meizi()
    #test_wuliao()
