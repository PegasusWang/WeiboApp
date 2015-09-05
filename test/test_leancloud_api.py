#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from db.leancloud_api import LeanCloudApi


def callback(res):
    for i in res:
        print i.get('ID')


def test():
    l = LeanCloudApi("Girls")
    l.upload_file_by_url('test', url='http://ac-0pdchyat.clouddn.com/b73dfdfecfeaf84e.gif')


if __name__ == '__main__':
    test()
