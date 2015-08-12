#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
from crawler import Spider
from bs4 import BeautifulSoup


class GifakSpider(Spider):

    def get_gif(self, url='http://gifak-net.tumblr.com'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        div_list = soup.find_all('div', class_='article-content')
        img_list = [i.find('img') for i in div_list if i]
        url_list = [i.get('src') for i in img_list if i]
        return url_list

def test_gif():
    spider = GifakSpider()
    duanzi_list = spider.get_gif()
    for each in duanzi_list:
        print each


def main():
    test_gif()

if __name__ == '__main__':
    main()
