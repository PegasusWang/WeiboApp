#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..crawler import Spider
from ..tumblr_api import TumblrApi
from bs4 import BeautifulSoup
import lxml
import re
import requests
import time


# for recursive fetch
def fetch_html(url, retries=5):
    try:
        html = requests.get(url, timeout=20).text
    except:
        if retries > 0:
            print 'fetching...', retries, url
            time.sleep(3)
            return fetch_html(url, retries-1)
        else:
            print 'fetch failed', url
            return ''
    return html


def get_media_url_list(url):
    if not url:
        return []
    print 'fetch html...', url
    html = fetch_html(url)
    if not html:
        return []
    soup = BeautifulSoup(html, 'lxml')
    img_tag_list = soup.find_all('img')
    url_list = [i.get('src') for i in img_tag_list if i]
    return set(url_list)


class OfnaturesbeautySpider(Spider):
    def get_img(self, url='http://ofnaturesbeauty.tumblr.com/'):
        img_list = get_media_url_list(url)
        img_list = [i.replace('250', '1280') for i in img_list if 'media.tumblr' in i]
        return set([i for i in img_list if 'avatar' not in i])
