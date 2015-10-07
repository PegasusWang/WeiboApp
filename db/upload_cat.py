#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import config
import os
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process
from ..crawler.animal.animals_tumblr import (
    CatOverloadSpider,
)


class Upload(object):
    def __init__(self, **kwargs):
        self.upload_type = kwargs.get('upload_type')
        self.class_name = kwargs.get('class_name')
        self._upload = LeanCloudApi(self.class_name)
        self.map_method = {
            'upload_cat': self.upload_cat,
        }

    def upload(self, **args):
        func_name = 'upload_' + self.upload_type
        func = self.map_method.get(func_name)
        print 'func', func
        if func:
            func(**args)

    @staticmethod
    def get_file_list(root_dir):
        l = []
        list_dirs = os.walk(root_dir)
        for root, dirs, files in list_dirs:
            for f in files:
                l.append(os.path.join(root, f))
        return l

    @staticmethod
    def get_filename(file_abspath):
        """without suffix"""
        return file_abspath.rsplit('.', 1)[-2].rsplit('/', 1)[-1]

    @staticmethod
    def get_file_mimetype(file_abspath):
        return mimetypes.guess_type(file_abspath)[0]

    def upload_cat(self, **kwargs):
        beg, end = 1, 2000
        for i in range(beg, end+1):
            time.sleep(3)
            url = 'http://cat-overload.tumblr.com/page/%s' % i
            print url
            leancloud_upload = self._upload
            spider = CatOverloadSpider()
            img_list = spider.get_img(url)

            if len(img_list) < 10:
                break

            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.exist_file(filename):
                        continue
                    if leancloud_upload.is_img_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(3)

dict_list = [
    dict(upload_type='cat', class_name='CatOverload'),
]


@single_process
def main():
    for each in dict_list:
        u = Upload(**each)
        u.upload(**each)


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
