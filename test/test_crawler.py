#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setup
from crawler.funnygif.jiandan_crawler import JiandanSpider
from crawler.girl.girls_tumblr import HotgirlsfcSpider
from crawler.funnygif.funnygif_tumblr import (
    GifsboomSpider, GifsonSpider,
)

map_spider = {
    'JiandanSpider': JiandanSpider,
    'HotgirlsfcSpider': HotgirlsfcSpider,
    'GifsboomSpider': GifsboomSpider,
    'GifsonSpider': GifsonSpider,
}


class SpiderTest(object):
    def __init__(self, *args, **kwargs):
        self._class = map_spider[kwargs.get('class_name')]
        url = kwargs.get('url', None)
        cookies = kwargs.get('cookies', None)
        self.s = self._class(url, cookies)

    def test_spider_method(self, method_name=None, args=None):
        func = getattr(self.s, method_name)
        print func
        if args:
            return func(args)
        else:
            return func()


spider_list_dict = [
    dict(class_name='HotgirlsfcSpider', method_name='get_img'),
    dict(class_name='JiandanSpider', url='', cookies='757477302=453; bad-click-load=off; nsfw-click-load=off; gif-click-load=off; _gat=1; 757477302=433; _ga=GA1.2.784043191.1438269751; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1438270942,1438270944,1438270947,1438995506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1439110556',
         method_name='get_meizi'),
    dict(class_name='GifsboomSpider', method_name='get_gif'),
    dict(class_name='GifsonSpider', method_name='get_gif'),

]


def test_all():
    for each_s in spider_list_dict:
        spider = SpiderTest(**each_s)
        print spider.test_spider_method(each_s['method_name'])



def test():
    s = spider_list_dict[3]
    spider = SpiderTest(**s)
    l = spider.test_spider_method(s['method_name'])
    for i in l:
        print i


if __name__ == '__main__':
    test()
