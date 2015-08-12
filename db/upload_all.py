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
from ..crawler.tumblr_forgifs_com_crawler import TumblrForgifsSpider


class Upload(object):
    def __init__(self, **kwargs):
        self.upload_type = kwargs.get('upload_type')
        self.class_name = kwargs.get('class_name')
        self._upload = LeanCloudApi(self.class_name)
        self.map_method = {
            'upload_local_file': self.upload_local_file,
            'upload_jiandan': self.upload_jiandan,
            'upload_tumblr_forgifs': self.upload_tumblr_forgifs,
        }

    def upload(self, **args):
        func_name = 'upload_' + self.upload_type
        func = self.map_method.get(func_name)
        print func
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

    def upload_local_file(self, file_dir):
        leancloud_upload = self._upload
        file_list = Upload.get_file_list(file_dir)
        for each_file in file_list:
            filename = os.path.basename(each_file)    # have suffix
            if leancloud_upload.is_img_file(filename) and \
                not leancloud_upload.exist_file(filename):
                    leancloud_upload.upload_file(each_file)
                    time.sleep(3)

    def upload_jiandan(self, **kwargs):
        """jiandan need cookies"""
        print kwargs
        leancloud_upload = self._upload
        cookies = '757477302=453; bad-click-load=off; nsfw-click-load=off; gif-click-load=off; _gat=1; 757477302=433; _ga=GA1.2.784043191.1438269751; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1438270942,1438270944,1438270947,1438995506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1439110556'
        spider = JiandanSpider('', cookies)
        func = getattr(spider, 'get_' + kwargs.get('typename'))
        print 'uplaod_jiandan', func
        img_list = func()
        for each_url in img_list:
            if each_url:
                each_url = each_url.replace('thumbnail', 'mw1024')
                if 'static' in each_url:
                    continue
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_forgifs(self, **kwargs):
        leancloud_upload = self._upload
        spider = TumblrForgifsSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

dict_list = [
    dict(upload_type='tumblr_forgifs', class_name='TumblrForgifs'),
    dict(upload_type='jiandan', class_name='JiandanMeizi', typename='meizi'),
    dict(upload_type='jiandan', class_name='JiandanWuliao', typename='wuliao'),
]


@single_process
def main():
    for each in dict_list:
        u = Upload(**each)
        u.upload(**each)


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
