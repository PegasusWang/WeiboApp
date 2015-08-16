#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import config
import os
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process
from ..crawler.girl.girls_tumblr import (
    HotgirlsfcSpider, MzituSpider, LovelyasiansSpider,
    KormodelsSpider, KoreangirlshdSpider,
)
from ..crawler.funnygif.funnygif_tumblr import GifsboomSpider


class Upload(object):
    def __init__(self, **kwargs):
        self.upload_type = kwargs.get('upload_type')
        self.class_name = kwargs.get('class_name')
        self._upload = LeanCloudApi(self.class_name)
        self.map_method = {
            'upload_hotgirlsfc': self.upload_hotgirlsfc,
            'upload_gifsboom': self.upload_gifsboom,
            'upload_mzitu': self.upload_mzitu,
            'upload_kormodels': self.upload_kormodels,
            'upload_koreangirlshd': self.upload_koreangirlshd,
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

    def upload_hotgirlsfc(self, **kwargs):
        beg, end = 49, 700
        for i in range(beg, end+1):
            url = 'http://hotgirlsfc.tumblr.com/page/%s' % i
            print url
            leancloud_upload = self._upload
            spider = HotgirlsfcSpider()
            img_list = spider.get_img(url)
            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.is_img_file(filename) and \
                        not leancloud_upload.exist_file(filename):
                            leancloud_upload.upload_file_by_url(filename, each_url)
                            time.sleep(2)

    def upload_gifsboom(self, **kwargs):
        beg, end = 1, 1678
        for i in range(beg, end+1):
            url = 'http://gifsboom.net/page/%s' % i
            print url
            leancloud_upload = self._upload
            spider = GifsboomSpider()
            img_list = spider.get_gif(url)
            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.is_img_file(filename) and \
                        not leancloud_upload.exist_file(filename):
                            leancloud_upload.upload_file_by_url(filename, each_url)
                            time.sleep(2)

    def upload_mzitu(self, **kwargs):
        beg, end = 1, 103
        for i in range(beg, end+1):
            time.sleep(3)
            url = 'http://mzitu.com/page/%s' % i
            print url
            leancloud_upload = self._upload
            spider = MzituSpider()
            img_list = spider.get_img(url)
            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.is_img_file(filename) and \
                        not leancloud_upload.exist_file(filename):
                            leancloud_upload.upload_file_by_url(filename, each_url)
                            time.sleep(2)

    def upload_kormodels(self, **kwargs):
        beg, end = 1, 197
        for i in range(beg, end+1):
            time.sleep(2)
            url = 'http://kormodels.tumblr.com/page/%s' % i
            print url
            leancloud_upload = self._upload
            spider = KormodelsSpider()
            img_list = spider.get_img(url)
            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.is_img_file(filename) and \
                        not leancloud_upload.exist_file(filename):
                            leancloud_upload.upload_file_by_url(filename, each_url)
                            time.sleep(2)

    def upload_koreangirlshd(self, **kwargs):
        beg, end = 3, 240
        for i in range(beg, end+1):
            time.sleep(3)
            url = 'http://koreangirlshd.com/page/%s' % i
            print '*************', url, '**************'
            leancloud_upload = self._upload
            spider = KoreangirlshdSpider()
            img_list = spider.get_img(url)
            for each_url in img_list:
                if each_url:
                    print each_url
                    filename = each_url
                    if leancloud_upload.is_img_file(filename) and \
                        not leancloud_upload.exist_file(filename):
                            leancloud_upload.upload_file_by_url(filename, each_url)
                            time.sleep(2)
dict_list = [
    #dict(upload_type='hotgirlsfc', class_name='Hotgirlsfc'),
    #dict(upload_type='gifsboom', class_name='Gifsboom'),
    #dict(upload_type='mzitu', class_name='Mzitu'),
    #dict(upload_type='lovelyasians', class_name='Lovelyasians'),
    #dict(upload_type='kormodels', class_name='Kormodels'),
    dict(upload_type='koreangirlshd', class_name='Koreangirlshd'),
]


@single_process
def main():
    for each in dict_list:
        u = Upload(**each)
        u.upload(**each)


if __name__ == '__main__':
    main()
    print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
