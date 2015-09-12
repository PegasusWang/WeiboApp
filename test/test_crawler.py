#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
from crawler.funnygif.jiandan_crawler import JiandanSpider
from crawler.girl.girls_tumblr import (
    HotgirlsfcSpider, MzituSpider, LovelyasiansSpider,
    KormodelsSpider, KoreangirlshdSpider, FerchoechoSpider,
    Girl2chickSpider, SnsdpicsSpider, PassionNipponesSpider,
    Sossex1Spider, HotcosplaychicksSpider, ForchiSpider,
    HappylimSpider, Touch45Spider, SilymarinSpider,
    ChioeveSpider, HotGirlsAsiaSpider, OshiriSpider, VisualangelSpider,
    Blendy99Spider, AdnisSpider, JoanpeperoSpider, AoababofanSpider,
    LegloveworldSpider, KawaiilegSpider, GanpukudouSpider,
    HeypantyhoseSpider, SexyLadyJapanSpider, SekkusuSpider,
    JacyliuSpider, GirlFixSpider,
)
from crawler.funnygif.funnygif_tumblr import (
    GifsboomSpider, GifsonSpider, LolgifruSpider,
    ElmontajistaSpider, IcachondeoSpider,
)
from crawler.animal.animals_tumblr import (
    AnimalGifHunterSpider, AlthingscuteSpider, JunkuploadSpider,
    CatsdogsblogSpider, AnimalspatronusgifsSpider,
)
from crawler.boy.boys_tumblr import (
    AllboysboysSpider, LobbuSpider,
)
from crawler.fashion.fashion_tumblr import (
    KoreanFashionSpider,
)
map_spider = {
    'GirlFixSpider': GirlFixSpider,
    'JacyliuSpider': JacyliuSpider,
    'SekkusuSpider': SekkusuSpider,
    'SexyLadyJapanSpider': SexyLadyJapanSpider,
    'HeypantyhoseSpider': HeypantyhoseSpider,
    'GanpukudouSpider': GanpukudouSpider,
    'KawaiilegSpider': KawaiilegSpider,
    'AdnisSpider': AdnisSpider,
    'LegloveworldSpider': LegloveworldSpider,
    'AoababofanSpider': AoababofanSpider,
    'JoanpeperoSpider': JoanpeperoSpider,
    'Blendy99Spider': Blendy99Spider,
    'VisualangelSpider': VisualangelSpider,
    'OshiriSpider': OshiriSpider,
    'HotGirlsAsiaSpider': HotGirlsAsiaSpider,
    'ChioeveSpider': ChioeveSpider,
    'SilymarinSpider': SilymarinSpider,
    'Touch45Spider': Touch45Spider,
    'LobbuSpider': LobbuSpider,
    'KoreanFashionSpider': KoreanFashionSpider,
    'HappylimSpider': HappylimSpider,
    'JiandanSpider': JiandanSpider,
    'HotgirlsfcSpider': HotgirlsfcSpider,
    'GifsboomSpider': GifsboomSpider,
    'GifsonSpider': GifsonSpider,
    'MzituSpider': MzituSpider,
    'LovelyasiansSpider': LovelyasiansSpider,
    'KormodelsSpider': KormodelsSpider,
    'KoreangirlshdSpider': KoreangirlshdSpider,
    'FerchoechoSpider': FerchoechoSpider,
    'Girl2chickSpider': Girl2chickSpider,
    'SnsdpicsSpider': SnsdpicsSpider,
    'AnimalGifHunterSpider': AnimalGifHunterSpider,
    'AlthingscuteSpider': AlthingscuteSpider,
    'JunkuploadSpider': JunkuploadSpider,
    'CatsdogsblogSpider': CatsdogsblogSpider,
    'AnimalspatronusgifsSpider': AnimalspatronusgifsSpider,
    'LolgifruSpider': LolgifruSpider,
    'ElmontajistaSpider': ElmontajistaSpider,
    'PassionNipponesSpider': PassionNipponesSpider,
    'Sossex1Spider': Sossex1Spider,
    'HotcosplaychicksSpider': HotcosplaychicksSpider,
    'ForchiSpider': ForchiSpider,
    'IcachondeoSpider': IcachondeoSpider,
    'AllboysboysSpider': AllboysboysSpider,
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
    dict(class_name='GirlFixSpider', method_name='get_img'),
    dict(class_name='JacyliuSpider', method_name='get_img'),
    dict(class_name='SekkusuSpider', method_name='get_img'),
    dict(class_name='SexyLadyJapanSpider', method_name='get_img'),
    dict(class_name='HeypantyhoseSpider', method_name='get_img'),
    dict(class_name='GanpukudouSpider', method_name='get_img'),
    dict(class_name='KawaiilegSpider', method_name='get_img'),
    dict(class_name='JoanpeperoSpider', method_name='get_img'),
    dict(class_name='LegloveworldSpider', method_name='get_img'),
    dict(class_name='AdnisSpider', method_name='get_img'),
    dict(class_name='AoababofanSpider', method_name='get_img'),
    dict(class_name='Blendy99Spider', method_name='get_img'),
    dict(class_name='VisualangelSpider', method_name='get_img'),
    dict(class_name='OshiriSpider', method_name='get_img'),
    dict(class_name='HotGirlsAsiaSpider', method_name='get_img'),
    dict(class_name='ChioeveSpider', method_name='get_img'),
    dict(class_name='SilymarinSpider', method_name='get_img'),
    dict(class_name='Touch45Spider', method_name='get_img'),
    dict(class_name='LobbuSpider', method_name='get_img'),
    dict(class_name='KoreanFashionSpider', method_name='get_img'),
    dict(class_name='AllboysboysSpider', method_name='get_img'),
    dict(class_name='HotgirlsfcSpider', method_name='get_img'),
    dict(class_name='JiandanSpider', url='', cookies='757477302=453; bad-click-load=off; nsfw-click-load=off; gif-click-load=off; _gat=1; 757477302=433; _ga=GA1.2.784043191.1438269751; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1438270942,1438270944,1438270947,1438995506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1439110556',
         method_name='get_meizi'),
    dict(class_name='GifsboomSpider', method_name='get_gif'),
    dict(class_name='GifsonSpider', method_name='get_gif'),
    dict(class_name='MzituSpider', method_name='get_img'),
    dict(class_name='LovelyasiansSpider', method_name='get_img'),
    dict(class_name='KormodelsSpider', method_name='get_img'),
    dict(class_name='KoreangirlshdSpider', method_name='get_img'),
    dict(class_name='FerchoechoSpider', method_name='get_img'),
    dict(class_name='Girl2chickSpider', method_name='get_img'),
    dict(class_name='SnsdpicsSpider', method_name='get_img'),
    dict(class_name='AnimalGifHunterSpider', method_name='get_img'),
    dict(class_name='AlthingscuteSpider', method_name='get_img'),
    dict(class_name='JunkuploadSpider', method_name='get_img'),
    dict(class_name='CatsdogsblogSpider', method_name='get_img'),
    dict(class_name='AnimalspatronusgifsSpider', method_name='get_img'),
    dict(class_name='LolgifruSpider', method_name='get_gif'),
    dict(class_name='ElmontajistaSpider', method_name='get_gif'),
    dict(class_name='PassionNipponesSpider', method_name='get_img'),
    dict(class_name='Sossex1Spider', method_name='get_img'),
    dict(class_name='HotcosplaychicksSpider', method_name='get_img'),
    dict(class_name='ForchiSpider', method_name='get_img'),
    dict(class_name='IcachondeoSpider', method_name='get_gif'),
    dict(class_name='HappylimSpider', method_name='get_img'),
]


def test_all():
    for each_s in spider_list_dict:
        spider = SpiderTest(**each_s)
        print spider.test_spider_method(each_s['method_name'])

def test_spider(class_name, method_name, url='', cookies=''):
    spider = SpiderTest(class_name=class_name)
    l = spider.test_spider_method(method_name)
    for i in l:
        print i

def test():
    s = spider_list_dict[0]
    spider = SpiderTest(**s)
    l = spider.test_spider_method(s['method_name'])
    for i in l:
        print i
    print len(l)


if __name__ == '__main__':
    test()
