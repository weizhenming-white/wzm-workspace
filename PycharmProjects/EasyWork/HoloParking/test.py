#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-05-28 17:39
brief:test
"""

import time
import datetime

now = int(time.time())  # 1533952277
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print otherStyleTime.split(" ")[0]