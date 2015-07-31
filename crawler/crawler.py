#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback
from bs4 import BeautifulSoup


class Spider(object):
    """base Spder class."""
    def __init__(self, url):
        self._url = url

    def get_html(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        try:
            html = requests.get(self._url, headers=headers, timeout=10).text
        except:
            html = ''
            traceback.print_exc()
        return html

class S(Spider):
    pass


def test_crawler():
    url = "http://m.qiushibaike.com/text"
    #spider = Spider(url)
    spider = S(url)
    print spider.get_html()


if __name__ == '__main__':
    test_crawler()
