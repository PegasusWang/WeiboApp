#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis import StrictRedis
import random


def init():
    r = StrictRedis('127.0.0.1', 6379)
    key = 'QQMAIL'
    mail_list = []
    with open('qq.txt', 'r') as f:
        for line in f:
            mail_list.append(line.strip())

    random.shuffle(mail_list)

    for i in mail_list:
        r.lpush(key, i)


if __name__ == '__main__':
    init()
