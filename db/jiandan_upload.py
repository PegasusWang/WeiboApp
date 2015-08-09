#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import config
import os
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process
from ..crawler.jiandan_crawler import JiandanSpider


def get_file_list(root_dir):
    l = []
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        for f in files:
            l.append(os.path.join(root, f))
    return l


def get_filename(file_abspath):
    """without suffix"""
    return file_abspath.rsplit('.', 1)[-2].rsplit('/', 1)[-1]


def get_file_mimetype(file_abspath):
    return mimetypes.guess_type(file_abspath)[0]


def upload_all_file(class_name, file_dir):
    leancloud_upload = LeanCloudApi(class_name)
    file_list = get_file_list(file_dir)
    for each_file in file_list:
        filename = os.path.basename(each_file)    # have suffix
        if leancloud_upload.is_img_file(filename) and \
            not leancloud_upload.exist_file(filename):
                leancloud_upload.upload_file(each_file)
                time.sleep(3)

def upload_jiandan(typename, class_name):
    leancloud_upload = LeanCloudApi(class_name)
    if typename == 'meizi':
        beg = 900
        end = 1504
    else:
        beg = 4013
        end = 7079
    for i in range(beg, end+1):
        time.sleep(5)
        if typename == 'meizi':
            url = "http://jandan.net/ooxx/page-%s#comments" % str(i)
        else:
            url = "http://jandan.net/pic/page-%s#comments" % str(i)
        cookies = '757477302=453; bad-click-load=off; nsfw-click-load=off; gif-click-load=off; _gat=1; 757477302=433; _ga=GA1.2.784043191.1438269751; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1438270942,1438270944,1438270947,1438995506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1439110556'
        print url
        s = JiandanSpider(url, cookies)
        html = s.get_html()
        func = getattr(s, 'get_' + typename)
        print func
        img_list = func(html)
        for each_url in img_list:
            if each_url:
                filename = each_url
                each_url = each_url.replace('thumbnail', 'mw1024')
                if 'static' in each_url:
                    continue
                print each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

@single_process
def main():
    # upload_all_file('ImgFile', config.UPLOAD_DIR)
    upload_jiandan('wuliao', 'JiandanWuliao')


if __name__ == '__main__':
    main()
