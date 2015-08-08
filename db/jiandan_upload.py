#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

def upload_jiandan_meizi(class_name):
    leancloud_upload = LeanCloudApi(class_name)
    #for i in range(900, 1501):
    for i in range(900, 901):
        url = "http://jandan.net/ooxx/page-%s#comments" % str(i)
        print url
        s = JiandanSpider(url)
        html = s.get_html()
        img_list = s.get_meizi(html)
        for each in img_list:
            filename = url
            url = each.replace('thumbnail', 'mw1024')
            if 'static' in url:
                continue
            print url
            if not leancloud_upload.exist_file(filename):
                leancloud_upload.upload_file_by_url(filename, url)
                time.sleep(2)

@single_process
def main():
    #upload_all_file('ImgFile', config.UPLOAD_DIR)
    upload_jiandan_meizi('JiandanMeizi')


if __name__ == '__main__':
    main()
