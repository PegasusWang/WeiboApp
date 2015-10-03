#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env
import base64
import random
from tornado.web import RequestHandler
from tornado.escape import json_encode
from db.leancloud_api import LeanCloudApi
import uuid

class Img:
    WIDTH = 192
    LIMIT_NUM = 30


def gen_uuid_32():
    return str(uuid.uuid4()).replace('-', '')

class LeanClassHandler(RequestHandler):
    @property
    def _redis(self):
        return self.application._redis

    def get(self, *args):
        class_name = self.get_query_argument('class_name')
        print(class_name)
        width = Img.WIDTH
        uuid_str = gen_uuid_32()
        key = class_name + ':' + str(width)
        try:
            page = int(self.get_query_argument('page'))
        except:
            page = 1

        try:
            res_str = self._redis.hget(key, page)
        except:
            res_str = ''
        if res_str:
            res_b64 = base64.standard_b64encode(res_str)
            encrypt_str = uuid_str[:13] + res_b64 + uuid_str[:22]
            print 'from redis', page
            self.set_header("Content-Type", "text/plain")
            self.write(encrypt_str)

        else:
            l = LeanCloudApi(class_name)
            limit_num = Img.LIMIT_NUM

            obj_list = l.get_skip_obj_list(page-1, limit_num=limit_num)

            result = []
            for i in obj_list:
                img_ID = i.get('ID')
                img_url = i.get('File').url
                img_href = img_url.split('/')[-1].replace('.', '_')
                if 'gif' in img_href.lower():
                    img_url = img_url + '?vframe/jpg/offset/1|imageMogr2/thumbnail/%sx/interlace/1' % width
                else:
                    img_url = img_url + '?imageMogr2/thumbnail/%sx/interlace/1' % width


                ori_width = i.get('width')
                ori_height = i.get('height')
                try:
                    height = width*ori_height/ori_width
                    each_res = {'href': img_href, 'id': img_ID, 'image': img_url, 'width': width, 'height': height}
                except TypeError:
                    each_res = random.choice(default_res)

                result.append(each_res)

            res = {'total': limit_num, 'result': result}
            res_str = json_encode(res)

            try:
                self._redis.hset(key, page, res_str)
            except:
                pass
            res_b64 = base64.standard_b64encode(res_str)
            encrypt_str = uuid_str[:13] + res_b64 + uuid_str[:22]
            self.set_header("Content-Type", "text/plain")
            self.write(encrypt_str)


class LeanHandler(RequestHandler):
    @property
    def _redis(self):
        return self.application._redis

    def initialize(self, class_name, leancloud_db):
        self._leancloud_api = leancloud_db
        self._class_name = class_name

    def get(self, class_name=None):
        width = Img.WIDTH
        uuid_str = gen_uuid_32()
        key = self._class_name + ':' + str(width)
        try:
            page = int(self.get_query_argument('page'))
        except:
            page = 1

        try:
            res_str = self._redis.hget(key, page)
        except:
            res_str = ''
        if res_str:
            res_b64 = base64.standard_b64encode(res_str)
            encrypt_str = uuid_str[:13] + res_b64 + uuid_str[:22]
            self.write(encrypt_str)

        else:
            l = self._leancloud_api
            limit_num = Img.LIMIT_NUM

            obj_list = l.get_skip_obj_list(page-1, limit_num=limit_num)

            result = []
            for i in obj_list:

                img_ID = i.get('ID')
                img_url = i.get('File').url
                img_url = img_url + '?imageMogr2/thumbnail/%sx' % width
                ori_width = i.get('width')
                ori_height = i.get('height')
                try:
                    height = width*ori_height/ori_width
                    each_res = {'id': img_ID, 'image': img_url, 'width': width, 'height': height}
                except TypeError:
                    each_res = random.choice(default_res)

                result.append(each_res)

            res = {'total': limit_num, 'result': result}
            res_str = json_encode(res)

            try:
                self._redis.hset(key, page, res_str)
            except:
                pass
            res_b64 = base64.standard_b64encode(res_str)
            encrypt_str = uuid_str[:13] + res_b64 + uuid_str[:22]
            self.set_header("Content-Type", "text/plain")
            self.write(encrypt_str)


default_res =[
{"width": 340, "image": "http://ac-0pdchyat.clouddn.com/2d5b60ee4529704.jpg?imageMogr2/thumbnail/340x", "height": 469}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/458daf53f729ec5.jpg?imageMogr2/thumbnail/340x", "height": 227}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/1851db831c4b1d8.jpg?imageMogr2/thumbnail/340x", "height": 508}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/996094a9fed8c53f.jpg?imageMogr2/thumbnail/340x", "height": 453}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/7c8fcbe22cdac853.jpg?imageMogr2/thumbnail/340x", "height": 390}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/dff0bf689a238e12.jpg?imageMogr2/thumbnail/340x", "height": 490}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/9ccd46bc29bfb87.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/ad312b5e9f7a1d89.png?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/5c1e86bcde4788.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/48f26c4b15458326.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/3e48aee7a726ad09.jpg?imageMogr2/thumbnail/340x", "height": 335}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/df472cd85d75484d.jpg?imageMogr2/thumbnail/340x", "height": 511}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/6256dda84e7ce2c.jpg?imageMogr2/thumbnail/340x", "height": 434}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/b5ad61aba1016749.png?imageMogr2/thumbnail/340x", "height": 487}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/62c2c7b4b232234.jpg?imageMogr2/thumbnail/340x", "height": 241}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/92178001ad1c7316.jpg?imageMogr2/thumbnail/340x", "height": 226}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e0bc9c75dd4911be.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/5a7eefd5c3da61b.jpg?imageMogr2/thumbnail/340x", "height": 219}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/c4279f2766682197.jpg?imageMogr2/thumbnail/340x", "height": 227}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/18e2c63abf18d246.jpg?imageMogr2/thumbnail/340x", "height": 467}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/7c9a260bb272188c.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/1886cd939f2f5061.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/15aec90b0dc691e.jpg?imageMogr2/thumbnail/340x", "height": 191}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/f824d0c174b38208.jpg?imageMogr2/thumbnail/340x", "height": 457}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/22dd83a464017462.jpg?imageMogr2/thumbnail/340x", "height": 340}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e8d146ea35993829.jpg?imageMogr2/thumbnail/340x", "height": 427}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/97481a7a54be9efc.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/19d0c5a1b6e06598.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e6dcd75c257fa070.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/8f8e77bb4d35f125.jpg?imageMogr2/thumbnail/340x", "height": 484},
{"width": 340, "image": "http://ac-0pdchyat.clouddn.com/a73e9972f9915467.jpg?imageMogr2/thumbnail/340x", "height": 433}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e7edeaf419b2852e.jpg?imageMogr2/thumbnail/340x", "height": 495}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/6fd4dc5c284fb45a.jpg?imageMogr2/thumbnail/340x", "height": 450}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/4c9494b3ef5ffba0.jpg?imageMogr2/thumbnail/340x", "height": 511}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/83a71b0253449a.jpg?imageMogr2/thumbnail/340x", "height": 191}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/41c8414d1c07b70.jpg?imageMogr2/thumbnail/340x", "height": 239}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/ca0b9e75887ba222.jpg?imageMogr2/thumbnail/340x", "height": 256}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/c8f1a2995abc7e9f.jpg?imageMogr2/thumbnail/340x", "height": 242}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/fea6b96612e5b381.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/3532c0c6d8ea4a.jpg?imageMogr2/thumbnail/340x", "height": 617}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/f2ec7cff4d75883.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/6c51237fdb0ee6.jpg?imageMogr2/thumbnail/340x", "height": 569}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/bd9da6382b8135d4.jpg?imageMogr2/thumbnail/340x", "height": 220}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/784015b980236f5.jpg?imageMogr2/thumbnail/340x", "height": 446}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/7fe15ed1a2543989.jpg?imageMogr2/thumbnail/340x", "height": 226}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/2771e4a5d26b30e6.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e786339198653fb0.jpg?imageMogr2/thumbnail/340x", "height": 486}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/a7fc2d6b25a53609.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/5fceb5bfbcdbe26.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/30c2a3b8c7ee9dc.jpg?imageMogr2/thumbnail/340x", "height": 566}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/bf74e9d1ecf93d2c.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/951e43b53142368.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/2d42df54f97a356f.jpg?imageMogr2/thumbnail/340x", "height": 467}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/4cedd30918d8000.jpg?imageMogr2/thumbnail/340x", "height": 436}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/f525fe625b9c33dc.jpg?imageMogr2/thumbnail/340x", "height": 225}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/e4837efedf5f480.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/8b19feb8e92a251c.jpg?imageMogr2/thumbnail/340x", "height": 627}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/6613785557d95882.jpg?imageMogr2/thumbnail/340x", "height": 479}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/f8c568e7e06b79ab.jpg?imageMogr2/thumbnail/340x", "height": 240}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/8ac820d14b524b7.jpg?imageMogr2/thumbnail/340x", "height": 218},
{"width": 340, "image": "http://ac-0pdchyat.clouddn.com/be896f66d89af4bc.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/c97bde4975418af9.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/752746f3333121f2.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/55c05f14d71ab354.jpg?imageMogr2/thumbnail/340x", "height": 450}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/8a32586fef8daf15.jpg?imageMogr2/thumbnail/340x", "height": 242}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/594dcb9cba75b372.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/74e0ae91cec6909.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/c51c4b3faa1e8d3b.jpg?imageMogr2/thumbnail/340x", "height": 226}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/13c0f0f15ed26df7.jpg?imageMogr2/thumbnail/340x", "height": 448}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/8b0dcba577be211.jpg?imageMogr2/thumbnail/340x", "height": 524}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/def6af01956d846a.jpg?imageMogr2/thumbnail/340x", "height": 503}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/da2f205076938e6.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/684957ffe36e7d3c.jpg?imageMogr2/thumbnail/340x", "height": 512}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/60f183befadf84f0.jpg?imageMogr2/thumbnail/340x", "height": 453}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/37944c9465845cab.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/b89ee20d9568a490.jpg?imageMogr2/thumbnail/340x", "height": 523}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/cc6ef3506083197a.png?imageMogr2/thumbnail/340x", "height": 482}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/27936c722fcf8e2a.jpg?imageMogr2/thumbnail/340x", "height": 451}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/b576abd3e6d74273.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/a5376a78cac3a7.jpg?imageMogr2/thumbnail/340x", "height": 510}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/6ba2d11c1eb435c.jpg?imageMogr2/thumbnail/340x", "height": 222}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/16867eb42a9565.jpg?imageMogr2/thumbnail/340x", "height": 512}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/1571cbb5ccfbf367.jpg?imageMogr2/thumbnail/340x", "height": 479}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/652313fe16a0bbed.jpg?imageMogr2/thumbnail/340x", "height": 543}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/91f8615d37d912bf.jpg?imageMogr2/thumbnail/340x", "height": 472}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/dfd79721d6bf86.jpg?imageMogr2/thumbnail/340x", "height": 511}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/671ee3949267f27e.jpg?imageMogr2/thumbnail/340x", "height": 495}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/24d3d0ef49819bb1.jpg?imageMogr2/thumbnail/340x", "height": 484}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/9509d3d87e346feb.jpg?imageMogr2/thumbnail/340x", "height": 529}, {"width": 340, "image": "http://ac-0pdchyat.clouddn.com/71482a509184aafd.jpg?imageMogr2/thumbnail/340x", "height": 512},
]
