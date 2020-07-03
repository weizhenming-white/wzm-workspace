#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-05-28 17:39
brief:test
"""

import time
import datetime

# 时间戳转换
# now = int(time.time())  # 1533952277
# timeArray = time.localtime(now)
# otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print otherStyleTime.split(" ")[0]

print time.time()

a = [5, 2, 6, 9, 111, 99]
for i in range(len(a)):
    min_idx = i
    # print i
    for j in range(i + 1, len(a)):
        print j
        if a[i] > a[j]:
            min_idx = j
    
    a[i], a[min_idx] = a[min_idx], a[i]
print a