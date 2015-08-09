#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
import config
import StringIO
import requests
import random
from crawler.qiubai_crawler import QiubaiSpider
from db import leancloud_api
from weibo_app import WeiboApp


class WeiboTypes(object):

    def __init__(self, weibo_app):
        self.weibo_app = weibo_app
        self.map_method = {
            'get_gif_file': self.get_gif_file,
            'get_qiubai_hot': self.get_qiubai_hot,
            'get_qiubai_img': self.get_qiubai_img,
            'get_qiubai_duanzi': self.get_qiubai_duanzi,
        }

    def choose(self, type_name):
        func_name = 'get_' + type_name
        func = self.map_method.get(func_name)
        func()

    def get_gif_file(self):
        upload = leancloud_api.LeanCloudApi('ImgFile')
        d = upload.get_imgfile_by_recent_ID()
        self.weibo_app.post_img(d.get('content'), d.get('pic'))

    def get_qiubai_hot(self):
        url = "http://m.qiushibaike.com/hot/page"
        s = QiubaiSpider(url)
        html = s.get_html()
        l = s.get_hot(html)
        i = random.choice(l)
        img_url = i.get('img')
        #print i.get('content'), img_url
        print img_url
        pic = StringIO.StringIO(requests.get(img_url).content)
        self.weibo_app.post_img(i.get('content'), pic)

    def get_qiubai_img(self):
        url = "http://m.qiushibaike.com/imgrank"
        s = QiubaiSpider(url)
        html = s.get_html()
        l = s.get_img(html)
        i = random.choice(l)
        img_url = i.get('img')
        #print i.get('content'), img_url
        print img_url
        pic = StringIO.StringIO(requests.get(img_url).content)
        self.weibo_app.post_img(i.get('content'), pic)

    def get_qiubai_duanzi(self):
        url = "http://m.qiushibaike.com/text"
        s = QiubaiSpider(url)
        html = s.get_html()
        l = s.get_hot(html)
        i = random.choice(l)
        self.weibo_app.post_text(i.get('content'))
