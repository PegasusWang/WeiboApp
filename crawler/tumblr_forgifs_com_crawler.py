#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
from crawler import Spider
from bs4 import BeautifulSoup


class TumblrForgifsSpider(Spider):

    def get_gif(self, html):
        soup = BeautifulSoup(html, 'lxml')
        media_list = soup.find_all('div', class_='media')
        img_list = [i.find('img') for i in media_list]
        url_list = [i.get('src') for i in img_list]
        return url_list

def test_gif():
    for i in range(1, 2):
        url = 'http://tumblr.forgifs.com/page/%s' % i
        print url
        spider = TumblrForgifsSpider(url)
        html = spider.get_html()
        duanzi_list = spider.get_gif(html)
        """
        for each in duanzi_list:
            # print each.get('author'), each.get('content')
            print len(each.get('content'))
            print each.get('content')

        """

def main():
    test_gif()

if __name__ == '__main__':
    main()
