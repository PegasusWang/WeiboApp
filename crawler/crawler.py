#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback


class Spider(object):
    """base Spder class."""
    def __init__(self, url=None, cookies_str=None):
        self.url = url
        self.cookies_str = cookies_str

    def parse_cookies(self):
        d = {}
        l = self.cookies_str.split(';')
        for each in l:
            k = each.split('=')[0]
            v = each.split('=')[1]
            d[k] = v
        return d

    def get_html(self, url=None, retries=3):
        if url:
            self.url = url
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36'
        headers = {'User-Agent': user_agent}
        try:
            if self.cookies_str:
                cookies = self.parse_cookies()
                html = requests.get(self.url, headers=headers, cookies=cookies,
                                    timeout=10).text
            else:
                html = requests.get(self.url, headers=headers,
                                    timeout=10).text

        except:
            if retries > 0:
                print 'fetching...', retries
                return self.get_html(url, retries-1)
            else:
                print 'get html failed', url
                html = ''
                return html
        return html
