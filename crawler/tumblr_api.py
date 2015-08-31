#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import traceback
try:
    import simplejson as json
except ImportError:
    import json


class TumblrApi(object):

    def __init__(self, url=None):
        """url = 'http://hot-girls-asia.tumblr.com/api/read/json?start=0' """
        self.url = url

    def get_html(self, url=None, retries=5):
        if url:
            self.url = url
        try:
                html = requests.get(self.url, timeout=10).text
        except:
            if retries > 0:
                print 'get_html fetching...', retries, url
                time.sleep(3)
                return self.get_html(url, retries-1)
            else:
                print 'get html failed', url
                html = ''
                return html
        return html

    def get_json_from_url(self, url=None):
        if url:
            self.url = url
        l = self.get_html(self.url).strip()
        ind = l.find('{')
        return l[ind:-1]

    def get_posts_total(self):
        json_data = self.get_json_from_url(self.url)
        o = json.loads(json_data)
        post_total = o.get('posts-total')
        return int(post_total)

    def get_img_set(self):
        json_data = self.get_json_from_url(self.url)
        o = json.loads(json_data)
        posts = o.get('posts', [])
        url_set = set()
        for each_post in posts:
            url = each_post.get('photo-url-1280')
            url_set.add(url)
        return url_set
