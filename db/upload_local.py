#!/usr/bin/env python
# -*- coding:utf-8 -*-

import config
import os
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process


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


@single_process
def main():
    class_name_list = ['ImgFile', 'Girls']
    for class_name, each_dir in zip(class_name_list, config.UPLOAD_DIR):
        upload_all_file(class_name, each_dir)
    print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))


if __name__ == '__main__':
    main()
    # test()
