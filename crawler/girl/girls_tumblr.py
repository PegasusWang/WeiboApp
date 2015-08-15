#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..crawler import Spider
from bs4 import BeautifulSoup


class HotgirlsfcSpider(Spider):

    def get_img(self, url='http://hotgirlsfc.tumblr.com/'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        media_list = soup.find_all('div', class_='img')
        img_list = [i.find('img') for i in media_list if i]
        url_list = [i.get('src') for i in img_list if i]
        return url_list


class MzituSpider(Spider):

    def get_img(self, url='http://www.mzitu.com/'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        img_list = soup.find_all('img', class_='lazy')
        url_list = [i.get('data-original') for i in img_list if i]
        return url_list
