#!/usr/bin/env python
# -*- coding: utf-8 -*-

import leancloud_api
import requests
import time
import sys
try:
    import simplejson as json
except ImportError:
    import json


def fetch_data(url, retries=5):
    try:
        data = requests.get(url, timeout=5)
    except:
        if retries > 0:
            print 'fetch...', retries, url
            time.sleep(3)
            return fetch_data(url, retries-1)
        else:
            print 'fetch failed', url
            data = None
            return data
    return data


def add_img_info(obj):
        img_url = obj.get('File').url
        img_info_url = img_url + '?imageInfo'
        r = fetch_data(img_info_url)

        if not r:
            return

        img_info = r.json()
        width = img_info.get('width', None)
        height = img_info.get('height', None)

        try:
            obj.set('height', height)
            obj.set('width', width)
            print 'saving info', obj.get('ID')
            obj.save()
        except:
            time.sleep(1)
            obj.set('height', height)
            obj.set('width', width)
            print 'saving info', obj.get('ID')
            obj.save()


def callback(res_list):
    for i in res_list:
        if i:
            add_img_info(i)


def solve(class_name, callback):
    l = leancloud_api.LeanCloudApi(class_name)
    l.solve_all_class_obj(callback)


def main():
    try:
        class_name = sys.argv[1].strip()
    except IndexError:
        class_name = 'Catsdogsblog'
    print class_name
    solve(class_name, callback)
    print class_name

if __name__ == '__main__':
    main()
    print '**********finish********'
