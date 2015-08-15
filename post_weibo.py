#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
import config
import random
import time
from weibo_app import WeiboApp
from weibo_types import WeiboTypes
from single_process import single_process


def generate_type_list(d):
    """d is dict of types, {'gif':10, 'png': 3}. d[k] is weight of k"""
    type_list = []
    for k, v in d.iteritems():
        l = [k] * v
        type_list.extend(l)
    return type_list


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

    types = {'qiubai_duanzi': 3, 'qiubai_hot': 1, 'qiubai_img': 3,
             'gif_file': 10, 'tumblr_gifak': 10, 'tumblr_forgifs':10}
    type_list = generate_type_list(types)
    cur_type = random.choice(type_list)

    weibo_type = WeiboTypes(weibo_app)
    weibo_type.choose(cur_type)


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
