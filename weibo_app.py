#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
import config
from weibo import Client


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
        self._c.post('statuses/update', status=text)

    def post_img(self, img_text, img_ori):
        self._c.post('statuses/upload', status=img_text, pic=img_ori)


def main():
    api_key = config.WeiboApp.APP_KEY
    api_secret = config.WeiboApp.APP_SECRET
    callback_url = config.WeiboApp.CALLBACK_URL
    username = config.WeiboApp.USERNAME
    password = config.WeiboApp.PASSWORD
    uid = config.WeiboApp.UID

    weibo_app = WeiboApp(api_key, api_secret, callback_url, username,
                         password, uid)
    text = '我同学喜欢上了和他玩得比较好的一女汉子， 有次女汉子去他家玩，之后他就很委婉地表白了说：“我妈挺喜欢你的（意思就是他妈以为她是他带回去的对象）。” 然后，女汉子就仰天长笑说了一句：“哈哈哈哈，还不快叫爸爸！'
    weibo_app.post_text(text)


if __name__ == '__main__':
    main()
