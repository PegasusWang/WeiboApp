#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
import config
import StringIO
import requests
import random
from weibo import Client
from crawler.qiubai_crawler import QiubaiSpider
from single_process import single_process
from db import leancloud_upload


class WeiboApp(object):
    """WeiboApp client."""
    def __init__(self, api_key, api_secret, callback_url, username,
                 password, uid):
        self._c = Client(api_key, api_secret, callback_url,
                         username=username, password=password)
        self._uid = uid

    def get_show(self):
        return self._c.get('users/show', uid=self._uid)

    def post_text(self, text):
        text = text if len(text) <= 139 else text[0:139]
        self._c.post('statuses/update', status=text)

    def post_img(self, text, img_ori):
        text = text if len(text) <= 139 else text[0:139]
        self._c.post('statuses/upload', status=text, pic=img_ori)


def post_weibo(weibo_app, cur_type):
    if cur_type == 'gif':
        # d = leancloud_upload.get_random_file()
        d = leancloud_upload.get_imgfile_by_recent_ID(100)
        #print d.get('content')
        weibo_app.post_img(d.get('content'), d.get('pic'))

        return
    if cur_type == 'duanzi':
        url = "http://m.qiushibaike.com/text"
    elif cur_type == 'hot':
        url = "http://m.qiushibaike.com/hot/page"
    else:
        url = "http://m.qiushibaike.com/imgrank"

    s = QiubaiSpider(url)
    html = s.get_html()

    if cur_type == 'duanzi':
        l = s.get_duanzi(html)
        i = random.choice(l)
        #print i.get('content')
        weibo_app.post_text(i.get('content'))

    else:
        if cur_type == 'hot':
            l = s.get_hot(html)
        else:
            l = s.get_img(html)
        i = random.choice(l)
        img_url = i.get('img')
        #print i.get('content'), img_url
        print img_url
        pic = StringIO.StringIO(requests.get(img_url).content)
        weibo_app.post_img(i.get('content'), pic)


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
    post_weibo(weibo_app, 'gif')


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
    main()
