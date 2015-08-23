#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setup
import _env
import config
import sys
from weibo_app import WeiboApp
from weibo_types import WeiboTypes

types = ['qiubai_duanzi', 'qiubai_hot', 'qiubai_img', 'gif_file'
         'tumblr_forgifs', 'tumblr_gifak']


def init_app():
    api_key = config.WeiboApp.APP_KEY
    api_secret = config.WeiboApp.APP_SECRET
    callback_url = config.WeiboApp.CALLBACK_URL
    username = config.WeiboApp.USERNAME
    password = config.WeiboApp.PASSWORD
    uid = config.WeiboApp.UID

    weibo_app = WeiboApp(api_key, api_secret, callback_url, username,
                         password, uid)
    return weibo_app


def test_type(type_name):
    weibo_app = init_app()
    weibo_type = WeiboTypes(weibo_app)
    weibo_type.choose(type_name)


def test_all_types():
    weibo_app = init_app()
    weibo_type = WeiboTypes(weibo_app)
    for each_type in types:
        weibo_type.choose(each_type)
        time.sleep(10)


if __name__ == '__main__':
    if sys.argv[1]:
        test_type(sys.argv[1])
    else:
        test_type('tumblr_happylim')
