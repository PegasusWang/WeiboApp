#!/usr/bin/env python
# -*- coding:utf-8 -*-

import _env
from db import config
import leancloud

leancloud.init(config.LeanCloud.WeiboApp_APP_ID,
               master_key=config.LeanCloud.WeiboApp_APP_MASTER_KEY)
