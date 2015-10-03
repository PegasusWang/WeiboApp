#!/usr/bin/env python
# -*- coding:utf-8 -*-

import leancloud
import leancloud_config

leancloud.init(leancloud_config.LeanCloud.APP_ID,
               master_key=leancloud_config.LeanCloud.APP_MASTER_KEY)
