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
    JacyliuSpider, GirlFixSpider, SmallPigSpider,
    MoreangelsSpider, DoumigirlsSpider, IdoljpSpider,
    TokujiroSpider, ThegirlnotnakedSpider, SexyInStockingsSpider,
    MuttsuriKusoyarouSpider,  ABeautifulGSpider,

)
from crawler.funnygif.funnygif_tumblr import (
    GifsboomSpider, GifsonSpider, LolgifruSpider,
    ElmontajistaSpider, IcachondeoSpider,
)
from crawler.animal.animals_tumblr import (
    AnimalGifHunterSpider, AlthingscuteSpider, JunkuploadSpider,
    CatsdogsblogSpider, AnimalspatronusgifsSpider, AwwwwCuteSpider,
)
from crawler.boy.boys_tumblr import (
    AllboysboysSpider, LobbuSpider, NoonakimSpider,
)
from crawler.fashion.fashion_tumblr import (
    KoreanFashionSpider,
)
from crawler.nature.nature_tumblr import (
    OfnaturesbeautySpider,

)
map_spider = {
    'OfnaturesbeautySpider': OfnaturesbeautySpider,
    'AwwwwCuteSpider': AwwwwCuteSpider,
    'NoonakimSpider': NoonakimSpider,
    'ABeautifulGSpider': ABeautifulGSpider,
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
    dict(class_name='OfnaturesbeautySpider', method_name='get_img'),
    dict(class_name='NoonakimSpider', method_name='get_img'),
    dict(class_name='ABeautifulGSpider', method_name='get_img'),
    dict(class_name='MuttsuriKusoyarouSpider', method_name='get_img'),
    dict(class_name='SexyInStockingsSpider', method_name='get_img'),
    dict(class_name='ThegirlnotnakedSpider', method_name='get_img'),
    dict(class_name='TokujiroSpider', method_name='get_img'),
    dict(class_name='IdoljpSpider', method_name='get_img'),
    dict(class_name='JacyliuSpider', method_name='get_img'),
    dict(class_name='DoumigirlsSpider', method_name='get_img'),
    dict(class_name='MoreangelsSpider', method_name='get_img'),
    dict(class_name='SmallPigSpider', method_name='get_img'),
    dict(class_name='GirlFixSpider', method_name='get_img'),
    dict(class_name='SekkusuSpider', method_name='get_img'),
    dict(class_name='SexyLadyJapanSpider', method_name='get_img'),
    dict(class_name='HeypantyhoseSpider', method_name='get_img'),
    dict(class_name='GanpukudouSpider', method_name='get_img'),
    dict(class_name='HotgirlsfcSpider', method_name='get_img'),
    dict(class_name='JiandanSpider', url='', cookies='757477302=453; bad-click-load=off; nsfw-click-load=off; gif-click-load=off; _gat=1; 757477302=433; _ga=GA1.2.784043191.1438269751; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1438270942,1438270944,1438270947,1438995506; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1439110556',
         method_name='get_meizi'),
    dict(class_name='GifsboomSpider', method_name='get_gif'),
    dict(class_name='GifsonSpider', method_name='get_gif'),
    dict(class_name='MzituSpider', method_name='get_img'),
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
