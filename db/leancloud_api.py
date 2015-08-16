#!/usr/bin/env python
# -*- coding:utf-8 -*-

import leancloud
from leancloud import Object, Query, File
from StringIO import StringIO
import config
import os
import mimetypes
import random
import time
import traceback
import requests
import jieba


class LeanCloudApi(object):

    def __init__(self, class_name):
        leancloud.init(config.LeanCloud.WeiboApp_APP_ID,
                       master_key=config.LeanCloud.WeiboApp_APP_MASTER_KEY)
        self._class = Object.extend(class_name)
        self._query = Query(self._class)

    def get_obj_by_ID(self, obj_ID):
        query = self._query
        query.equal_to('ID', obj_ID)
        obj = query.first()
        url = obj.get('File').url
        pic = StringIO(requests.get(url).content)
        content = obj.get('filename').split('.')[0]
        return {'pic': pic, 'content': content}

    def get_obj_by_rangeID(self, beg, end):
        query = self._query
        query.less_than_or_equal_to('ID', end)
        query.greater_than_or_equal_to('ID', beg)
        file_list = query.find()
        file_obj = random.choice(file_list)
        url = file_obj.get('File').url
        pic = StringIO(requests.get(url).content)
        content = file_obj.get('filename').split('.')[0]
        return {'pic': pic, 'content': content}

    def get_imgfile_by_recent_ID(self, nums=50):
        query = self._query
        query.descending('ID')
        query.limit(nums)
        file_list = query.find()
        file_obj = random.choice(file_list)
        url = file_obj.get('File').url
        pic = StringIO(requests.get(url).content)
        content = file_obj.get('filename').split('.')[0]
        return {'pic': pic, 'content': content}

    def exist_file(self, filename):
        """filename have suffix"""
        query = self._query
        query.equal_to('filename', filename)
        try:    # finded
            obj = query.first()
            print filename, '----existed----'
            return True
        except:    # not find
            return False

    @staticmethod
    def fetch_data(url, retries=5):
        try:
            data = requests.get(url, timeout=5).content
        except:
            if retries > 0:
                print 'fetch...', retries, url
                time.sleep(3)
                return LeanCloudApi.fetch_data(url, retries-1)
            else:
                print 'fetch failed', url
                return ''
        return data

    def upload_file_by_url(self, filename, url):
        data = LeanCloudApi.fetch_data(url)
        if not data:
            return
        f = File(filename, StringIO(data))
        img_file = self._class()
        img_file.set('File', f)
        img_file.set('filename', filename)
        try:
            img_file.save()
            print filename, '----uploaded----'
        except:
            print 'save file failed', url
            time.sleep(10)
            return

    def upload_file(self, file_abspath):
        filename = os.path.basename(file_abspath)    # filename have suffix
        with open(file_abspath, 'r') as f:
            upload_file = File(filename, f)
            upload_file.save()
            print 'uploaded', file_abspath
            img_file = self._class()
            img_file.set('File', upload_file)
            img_file.set('filename', filename)
            tag_list = LeanCloudApi.get_tag_list(filename)
            img_file.set('tag_list', tag_list)
            img_file.save()

    @staticmethod
    def is_img_file(filename):
        suffix = filename.split('.')[-1].lower()    # note: remember ingore case
        img_types = set(['jpg', 'png', 'gif', 'jpeg', 'bmp'])
        return suffix in img_types

    @staticmethod
    def get_tag_list(filename):
        txt = filename.split('.')[0]
        jieba.setLogLevel(60)
        seg_list = jieba.cut(txt)
        return [i for i in seg_list if len(i) >= 2]
