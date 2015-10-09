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

TXT = u"""http://jinritu.com"今日图片"""

class WeiboTypes(object):

    def __init__(self, weibo_app):
        self.weibo_app = weibo_app
        self.map_method = {
            # gif
            'get_gif_file': self.get_gif_file,
            'get_tumblr_forgifs': self.get_tumblr_forgifs,
            'get_tumblr_gifak': self.get_tumblr_gifak,
            'get_tumblr_gifsboom': self.get_tumblr_gifsboom,
            'get_tumblr_gifson': self.get_tumblr_gifson,
            'get_tumblr_aewae': self.get_tumblr_aewae,
            'get_tumblr_elmontajista': self.get_tumblr_elmontajista,
            'get_tumblr_icachondeo': self.get_tumblr_icachondeo,
            'get_tumblr_tychoon': self.get_tumblr_tychoon,

            # animals
            'get_tumblr_catsdogsblog': self.get_tumblr_catsdogsblog,
            'get_tumblr_althingscute': self.get_tumblr_althingscute,

            # qiubai
            'get_qiubai_hot': self.get_qiubai_hot,
            'get_qiubai_img': self.get_qiubai_img,
            'get_qiubai_duanzi': self.get_qiubai_duanzi,

            # girls
            'get_girls': self.get_girls,
            'get_tumblr_bestofasiangirls': self.get_tumblr_bestofasiangirls,
            'get_tumblr_chinabeauties': self.get_tumblr_chinabeauties,
            'get_tumblr_sossex1': self.get_tumblr_sossex1,
            'get_tumblr_happylim': self.get_tumblr_happylim,
            'get_tumblr_girl2chick': self.get_tumblr_girl2chick,
            'get_tumblr_lovelyasians': self.get_tumblr_lovelyasians,

            # boys
            'get_tumblr_lobbu': self.get_tumblr_lobbu,
        }

    def choose(self, type_name):
        func_name = 'get_' + type_name
        print func_name
        func = self.map_method.get(func_name)
        func()

    def get_gif_file(self):
        upload = leancloud_api.LeanCloudApi('ImgFile')
        d = upload.get_imgfile_by_recent_ID()
        self.weibo_app.post_img(d.get('content'), d.get('pic'))

    def get_tumblr_forgifs(self):
        upload = leancloud_api.LeanCloudApi('TumblrForgifs')
        d = upload.get_imgfile_by_recent_ID()
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_gifak(self):
        upload = leancloud_api.LeanCloudApi('TumblrForgifs')
        d = upload.get_imgfile_by_recent_ID()
        self.weibo_app.post_img(u'每日gif', d.get('pic'))


    def get_tumblr_gifsboom(self):
        upload = leancloud_api.LeanCloudApi('Gifsboom')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_gifson(self):
        upload = leancloud_api.LeanCloudApi('Gifson')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_aewae(self):
        upload = leancloud_api.LeanCloudApi('Aewae')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_elmontajista(self):
        upload = leancloud_api.LeanCloudApi('Elmontajista')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_icachondeo(self):
        upload = leancloud_api.LeanCloudApi('Icachondeo')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_tychoon(self):
        upload = leancloud_api.LeanCloudApi('Tychoon')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'每日gif', d.get('pic'))

    def get_tumblr_catsdogsblog(self):
        upload = leancloud_api.LeanCloudApi('Catsdogsblog')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'汪星人和喵星人', d.get('pic'))

    def get_tumblr_althingscute(self):
        upload = leancloud_api.LeanCloudApi('Althingscute')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(u'萌物', d.get('pic'))

    def get_qiubai_hot(self):
        url = "http://m.qiushibaike.com/hot/page"
        s = QiubaiSpider(url)
        l = s.get_hot(url)
        i = random.choice(l)
        img_url = i.get('img')
        print img_url
        pic = StringIO.StringIO(requests.get(img_url).content)
        self.weibo_app.post_img(i.get('content'), pic)

    def get_qiubai_img(self):
        url = "http://m.qiushibaike.com/imgrank"
        s = QiubaiSpider(url)
        l = s.get_img(url)
        i = random.choice(l)
        img_url = i.get('img')
        print img_url
        pic = StringIO.StringIO(requests.get(img_url).content)
        self.weibo_app.post_img(i.get('content'), pic)

    def get_qiubai_duanzi(self):
        url = "http://m.qiushibaike.com/text"
        s = QiubaiSpider(url)
        l = s.get_duanzi(url)
        i = random.choice(l)
        self.weibo_app.post_text(i.get('content'))

    def get_girls(self):
        upload = leancloud_api.LeanCloudApi('Girls')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_bestofasiangirls(self):
        upload = leancloud_api.LeanCloudApi('Bestofasiangirls')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_chinabeauties(self):
        upload = leancloud_api.LeanCloudApi('Chinabeauties')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_sossex1(self):
        upload = leancloud_api.LeanCloudApi('Sossex1')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_happylim(self):
        upload = leancloud_api.LeanCloudApi('Happylim')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_girl2chick(self):
        upload = leancloud_api.LeanCloudApi('Girl2chick')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_lovelyasians(self):
        upload = leancloud_api.LeanCloudApi('Lovelyasians')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))

    def get_tumblr_lobbu(self):
        upload = leancloud_api.LeanCloudApi('Lobbu')
        d = upload.get_imgfile_by_recent_ID(100)
        self.weibo_app.post_img(TXT, d.get('pic'))
