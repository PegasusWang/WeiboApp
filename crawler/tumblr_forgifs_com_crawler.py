#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
from crawler import Spider
from bs4 import BeautifulSoup


class TumblrForgifsSpider(Spider):

    def get_gif(self, url='http://tumblr.forgifs.com/'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        media_list = soup.find_all('div', class_='media')
        img_list = [i.find('img') for i in media_list]
        url_list = [i.get('src') for i in img_list]
        return url_list

def test_gif():
    spider = TumblrForgifsSpider()
    duanzi_list = spider.get_gif()
    for each in duanzi_list:
        print each


def main():
    test_gif()

if __name__ == '__main__':
    main()
