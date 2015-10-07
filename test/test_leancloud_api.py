#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from db.leancloud_api import LeanCloudApi


def callback(res):
    for i in res:
        print i.get('ID')


def test():
    l = LeanCloudApi("CatOverload")
    print(l.exist_file('http://40.media.tumblr.com/90793aa5507e1b28b89ee033bb7ca6f1/tumblr_nvqn3kD1fl1up2ssxo1_250.png'))


if __name__ == '__main__':
    test()
