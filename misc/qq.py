#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup



def fetch_html(url):
    html = requests.get(url).content
    print(html)
    return html

def parse_html(html):
    pat = re.compile(r'[1-9][0-9]{4,}')
    print re.findall(pat, html)

def main():
    url = 'http://www.qq8886.com/index.html'
    html = fetch_html(url)
    parse_html(html)

if __name__ == '__main__':
    main()
