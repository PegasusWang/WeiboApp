#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import config
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process
from ..crawler.boy.boys_tumblr import (
    AllboysboysSpider, LobbuSpider, NoonakimSpider,
)

map_class = {
    'AllboysboysSpider': AllboysboysSpider,
    'LobbuSpider': LobbuSpider,
    'NoonakimSpider': NoonakimSpider,
}


class Upload(object):
    def __init__(self, **kwargs):
        self.spider_name = kwargs.get('spider_name')
        self.class_name = kwargs.get('spider_name').replace('Spider', '')
        self._upload = LeanCloudApi(self.class_name)

    def upload_girls(self, **kwargs):
        leancloud_upload = self._upload
        spider = map_class.get(self.spider_name)()
        print '*************', self.spider_name, '**************'
        img_list = spider.get_img()
        for each_url in img_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.exist_file(filename):
                    continue
                if leancloud_upload.is_img_file(filename):
                    leancloud_upload.upload_file_by_url(filename, each_url)
                    time.sleep(2)

    @staticmethod
    def get_filename(file_abspath):
        """without suffix"""
        return file_abspath.rsplit('.', 1)[-2].rsplit('/', 1)[-1]

    @staticmethod
    def get_file_mimetype(file_abspath):
        return mimetypes.guess_type(file_abspath)[0]


@single_process
def main():
    for k, v in map_class.iteritems():
        u = Upload(spider_name=k)
        u.upload_girls()


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time()))
