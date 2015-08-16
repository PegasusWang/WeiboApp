#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..crawler import Spider
from bs4 import BeautifulSoup
import lxml
import requests


def get_img_url_list(url):
    html = requests.get(url, timeout=5).text
    soup = BeautifulSoup(html, 'lxml')
    img_tag_list = soup.find_all('img')
    url_list = [i.get('src') for i in img_tag_list if i]
    return url_list


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


class LovelyasiansSpider(Spider):
    def get_img(self, url='http://lovely-asians.tumblr.com'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        img_list = soup.find_all('img')
        url_list = [i.get('src') for i in img_list if i]
        url_list = [i for i in url_list if 'media.tumblr' in i]
        return url_list


class KormodelsSpider(Spider):
    def get_img(self, url='http://kormodels.tumblr.com/'):
        s = LovelyasiansSpider()
        return s.get_img(url)


class KoreangirlshdSpider(Spider):
    def get_img(self, url='http://koreangirlshd.com/'):
        self.url = url
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml')
        post_tag_list = soup.find_all('div', class_='entry-content')
        img_tag_list = [i.find('img') for i in post_tag_list if i]
        a_list = [i.find('a') for i in post_tag_list if i]
        url_list = [i.get('src') for i in img_tag_list if i]
        href_list = [i.get('href') for i in a_list if i]
        for each in href_list:
            url_list.extend(get_img_url_list(each))

        return url_list
