#!/usr/bin/env python
# -*- coding: utf-8 -*-

import leancloud_api
import requests
import time
try:
    import simplejson as json
except ImportError:
    import json


def callback(res_list):
    for i in res_list:
        img_url = i.get('File').url
        img_info_url = img_url + '?imageInfo'

        try:
            r = requests.get(img_info_url)
            img_info = r.json()
        except:
            time.sleep(1)
            r = requests.get(img_info_url)
            img_info = r.json()

        if img_info.get('error'):
            print 'get img_info failed', i.get('ID')
            continue
        else:
            height = img_info.get('height')
            width = img_info.get('width')
            try:
                i.set('height', height)
                i.set('width', width)
                i.save()
            except:
                time.sleep(1)
                i.set('height', height)
                i.set('width', width)
                i.save()
            time.sleep(0.3)
            print 'saving img_info of', i.get('ID')


def solve(class_name, callback):
    l = leancloud_api.LeanCloudApi(class_name)
    l.solve_all_class_obj(callback)


def main():
    solve('Girls', callback)

if __name__ == '__main__':
    main()
    print '**********finish****************'
