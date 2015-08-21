#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
import config
import os
import mimetypes
import time
from leancloud_api import LeanCloudApi
from single_process import single_process
from ..crawler.funnygif.jiandan_crawler import JiandanSpider
from ..crawler.funnygif.funnygif_tumblr import (
    TumblrForgifsSpider, GifakSpider, GifsboomSpider, GifsonSpider,
    LolgifruSpider, ElmontajistaSpider, TychoonSpider,
    AewaeSpider,
)


class Upload(object):
    def __init__(self, **kwargs):
        self.upload_type = kwargs.get('upload_type')
        self.class_name = kwargs.get('class_name')
        self._upload = LeanCloudApi(self.class_name)
        self.map_method = {
            'upload_local_file': self.upload_local_file,
            'upload_jiandan': self.upload_jiandan,
            'upload_tumblr_forgifs': self.upload_tumblr_forgifs,
            'upload_tumblr_gifak': self.upload_tumblr_gifak,
            'upload_tumblr_gifsboom': self.upload_tumblr_gifsboom,
            'upload_tumblr_gifson': self.upload_tumblr_gifson,
            'upload_tumblr_lolgifru': self.upload_tumblr_lolgifru,
            'upload_tumblr_elmontajista': self.upload_tumblr_elmontajista,
            'upload_tumblr_tychoon': self.upload_tumblr_tychoon,
            'upload_tumblr_aewae': self.upload_tumblr_aewae,
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

    def upload_tumblr_gifak(self, **kwargs):
        leancloud_upload = self._upload
        spider = GifakSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_gifsboom(self, **kwargs):
        leancloud_upload = self._upload
        spider = GifsboomSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_gifson(self, **kwargs):
        leancloud_upload = self._upload
        spider = GifsonSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_lolgifru(self, **kwargs):
        leancloud_upload = self._upload
        spider = LolgifruSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_elmontajista(self, **kwargs):
        leancloud_upload = self._upload
        spider = ElmontajistaSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_tychoon(self, **kwargs):
        leancloud_upload = self._upload
        spider = TychoonSpider()
        gif_list = spider.get_gif()
        for each_url in gif_list:
            if each_url:
                print each_url
                filename = each_url
                if leancloud_upload.is_img_file(filename) and \
                    not leancloud_upload.exist_file(filename):
                        leancloud_upload.upload_file_by_url(filename, each_url)
                        time.sleep(2)

    def upload_tumblr_aewae(self, **kwargs):
        leancloud_upload = self._upload
        spider = AewaeSpider()
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
    dict(upload_type='tumblr_aewae', class_name='Aewae'),
    dict(upload_type='tumblr_tychoon', class_name='Tychoon'),
    dict(upload_type='tumblr_elmontajista', class_name='Elmontajista'),
    dict(upload_type='tumblr_lolgifru', class_name='Lolgifru'),
    dict(upload_type='tumblr_forgifs', class_name='TumblrForgifs'),
    dict(upload_type='tumblr_gifak', class_name='TumblrGifak'),
    dict(upload_type='tumblr_gifsboom', class_name='Gifsboom'),
    dict(upload_type='tumblr_gifson', class_name='Gifson'),
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
