#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler import Spider
import os
import re
import requests
from bs4 import BeautifulSoup
import traceback
import lxml


class JiandanSpider(Spider):

    def get_meizi(self, html):
        soup = BeautifulSoup(html, 'lxml')
        img_tag_list = soup.find_all('img')
        img_url_list = [i.get('src') for i in img_tag_list]
        print img_url_list


def test():
    url = 'http://jandan.net/ooxx/page-1485#comments'
    s = JiandanSpider(url)
    html = s.get_html()
    s.get_meizi(html)


if __name__ == '__main__':
    test()


"""
def url_open(url):
    # req = urllib.request.Request(url)
    # response = urllib.request.urlopen(req)
    r = requests.get(url, headers=headers)
    return r.text


def get_page(url):
    #html = url_open(url).decode('utf-8')
    html = url_open(url)
    # 正则表达式寻找页面地址
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>'
    page = int(re.findall(pattern, html)[0])
    return page


def find_imgs(page_url):
    pattern = r'<img src="(.*?\.jpg)"'
    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern, html)
    return img_addrs


def save_imgs(img_addrs, page_num, folder):
    os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        filename = i.split('/')[-1]
        image = url_open(i)
        with open(filename, 'wb') as f:
            f.write(image)


def download_mm(folder='./ooxx', pages=10):
    os.mkdir(folder) #新建文件夹
    os.chdir(folder) #跳转到文件夹
    folder_top = os.getcwd() #获取当前工作目录
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url) #获取网页最新的地址
    for i in range(pages):
        page_num -= i #递减下载几个网页
        page_url = url + 'page-' + str(page_num) + '#comments' #组合网页地址
        img_addrs = find_imgs(page_url) #获取图片地址
        save_imgs(img_addrs,page_num,folder) #保存图片
        os.chdir(folder_top)

if __name__ == '__main__':
    download_mm()
"""
