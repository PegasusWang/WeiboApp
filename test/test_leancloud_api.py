#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from db.leancloud_api import LeanCloudApi


def callback(res):
    for i in res:
        print i.get('ID')


def test():
    l = LeanCloudApi("Test")
    l.del_by_url('http://ac-0pdchyat.clouddn.com/fe045d1a630e7da1.png')


if __name__ == '__main__':
    test()
