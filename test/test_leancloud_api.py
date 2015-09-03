#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from db.leancloud_api import LeanCloudApi


def callback(res):
    for i in res:
        print i.get('ID')


def test():
    l = LeanCloudApi("Girls")
    l.solve_all_class_obj(callback)


if __name__ == '__main__':
    test()
