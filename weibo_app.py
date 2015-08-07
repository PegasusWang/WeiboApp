#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import _env
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
        text = text if len(text) <= 140 else text[0:140]
        self._c.post('statuses/update', status=text)

    def post_img(self, text, img_ori):
        text = text if len(text) <= 140 else text[0:140]
        self._c.post('statuses/upload', status=text, pic=img_ori)
