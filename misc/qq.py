#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from tornado import gen, httpclient, ioloop
import requests
from bs4 import BeautifulSoup
import time

BASE = 'http://www.qq8886.com'
URL = 'http://www.qq8886.com/index.html'

def get_urls(URL):
    html = requests.get(URL).content
    soup = BeautifulSoup(html)
    alla = (soup.find_all('a'))
    url_list = [i for i in alla if 'html' in i.get('href')]
    urls = []
    for i in url_list:
        urls.append(BASE + i.get('href'))
    return urls


class AsyncSpider(object):
    def __init__(self, urls):
        self.urls = urls

    @gen.coroutine
    def fetch_url(self, url):
        try:
            response = yield httpclient.AsyncHTTPClient().fetch(url)
        except:
            print 'fetch fail'
            raise gen.Return('')

        raise gen.Return(response.body)

    def handle_page(self, url, html):
        print(url)
        pat = re.compile(r'[1-9][0-9]{4,}')
        nums = re.findall(pat, html)
        res = [i for i in nums if '2015' not in i]
        with open('qq.txt', 'a+') as f:
            f.write("\n".join(res))
        for i in res:
            print i
        print(res)

    @gen.coroutine
    def _run(self):
        for url in self.urls:
            html = yield self.fetch_url(url)
            self.handle_page(url, html)

    def run(self):
        io_loop = ioloop.IOLoop.current()
        io_loop.run_sync(self._run)


if __name__ == '__main__':
    urls = get_urls(URL)
    s = AsyncSpider(urls)
    s.run()
