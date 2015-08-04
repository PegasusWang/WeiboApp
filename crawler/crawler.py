#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import traceback


class Spider(object):
    """base Spder class."""
    def __init__(self, url):
        self.url = url

    def get_html(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        try:
            html = requests.get(self.url, headers=headers, timeout=10).text
        except:
            html = ''
            traceback.print_exc()
        return html
