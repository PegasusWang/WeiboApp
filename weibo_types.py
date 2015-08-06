#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
import config
import StringIO
import requests
import random
from crawler.qiubai_crawler import QiubaiSpider
from single_process import single_process
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
        type_name = 'get_' + type_name
        fun = self.map_method.get(type_name)
        fun()

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

def generate_type_list(d):
    """d is dict of types, {'gif':10, 'png': 3}. d[k] is weight of k"""
    type_list = []
    for k, v in d.iteritems():
        l = [k] * v
        type_list.extend(l)
    return type_list


def test():
    api_key = config.WeiboApp.APP_KEY
    api_secret = config.WeiboApp.APP_SECRET
    callback_url = config.WeiboApp.CALLBACK_URL
    username = config.WeiboApp.USERNAME
    password = config.WeiboApp.PASSWORD
    uid = config.WeiboApp.UID

    weibo_app = WeiboApp(api_key, api_secret, callback_url, username,
                         password, uid)
    #post_weibo(weibo_app, 'gif')
    weibo_types = WeiboTypes(weibo_app)
    weibo_types.choose('gif_file')



@single_process
def main():
    api_key = config.WeiboApp.APP_KEY
    api_secret = config.WeiboApp.APP_SECRET
    callback_url = config.WeiboApp.CALLBACK_URL
    username = config.WeiboApp.USERNAME
    password = config.WeiboApp.PASSWORD
    uid = config.WeiboApp.UID

    weibo_app = WeiboApp(api_key, api_secret, callback_url, username,
                         password, uid)

    # types = ['duanzi', 'hot', 'img', 'gif', 'gif', 'gif']
    types = {'duanzi': 1, 'hot': 1, 'img': 1, 'gif': 10}
    type_list = generate_type_list(types)
    cur_type = random.choice(type_list)
    print cur_type
    post_weibo(weibo_app, cur_type)


if __name__ == '__main__':
    #main()
    test()
