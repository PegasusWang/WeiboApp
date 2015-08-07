#!/bin/bash

PREFIX=$(cd "$(dirname "$0")"; pwd)
cd $PREFIX

python post_weibo.py
