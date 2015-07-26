#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
import config
import StringIO
import requests
import random
from weibo import Client
from crawler.qiubai.qiubai_crawler import Spider as QiubaiSpider
from single_process import single_process


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
    post_types = ['duanzi', 'hot']
    cur_type = random.choice(post_types)

    if cur_type == 'duanzi':
        url = "http://m.qiushibaike.com/text"
        s = QiubaiSpider(url)
        html = s.get_html()
        duanzi_list = s.get_duanzi(html)
        duanzi = random.choice(duanzi_list)
        weibo_app.post_text(duanzi.get('content'))

    elif cur_type == 'hot':
        url = "http://m.qiushibaike.com/hot/page/1"
        s = QiubaiSpider(url)
        html = s.get_html()
        hot_list = s.get_hot(html)
        hot = random.choice(hot_list)
        img_url = hot.get('img')
        pic = StringIO.StringIO(requests.get(img_url).content)
        weibo_app.post_img(hot.get('content'), pic)


if __name__ == '__main__':
    main()
