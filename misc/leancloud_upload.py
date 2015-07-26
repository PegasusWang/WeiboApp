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
import requests
from single_process import single_process

leancloud.init(config.LeanCloud.WeiboApp_APP_ID,
               master_key=config.LeanCloud.WeiboApp_APP_MASTER_KEY)

ImgFile = Object.extend('ImgFile')


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


def upload_file(file_abspath):
    filename = os.path.basename(file_abspath)    # filename have suffix
    with open(file_abspath, 'r') as f:
        upload_file = File(filename, f)
        upload_file.save()
        print 'uploaded', file_abspath
        img_file = ImgFile()
        img_file.set('File', upload_file)
        img_file.set('filename', filename)
        img_file.save()


def get_random_file():
    query = Query(ImgFile)
    file_list = query.find()
    file_obj = random.choice(file_list)
    url = file_obj.get('File').url
    pic = StringIO(requests.get(url).content)
    content = file_obj.get('filename').split('.')[0]
    return {'pic': pic, 'content': content}


def get_imgfile_by_ID(file_id):
    query = Query(ImgFile)
    query.equal_to('ID', file_id)
    obj = query.first()
    url = obj.get('File').url
    pic = StringIO(requests.get(url).content)
    content = obj.get('filename').split('.')[0]
    return {'pic': pic, 'content': content}


def exist_file(filename):
    """filename have suffix"""
    query = Query(ImgFile)
    query.equal_to('filename', filename)
    try:    # finded
        obj = query.first()
        return True
    except:    # not find
        return False


def upload_all_file(file_dir='/home/wnn/share/gif'):
    file_list = get_file_list(file_dir)
    for each_file in file_list:
        filename = os.path.basename(each_file)    # have suffix
        if not exist_file(filename):
            upload_file(each_file)
            # time.sleep(3)


def test():
    d = get_random_file()
    print d.get('content')


@single_process
def main():
    upload_all_file()


if __name__ == '__main__':
    main()
    #test()