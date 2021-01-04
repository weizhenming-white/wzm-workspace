#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-23 16:26
brief:已知坐标值（x, y）,求该点的距离和角度
"""

import math
import os
import sys
import time

def value_to_angel():

    a = (3, 4)
    print math.tan(4/3)
    # print math.degrees(math.atan(math.sqrt(3) / 3))
    print math.atan(4/3)
    print math.pi / 4

    # 将反正切得到的弧度转化成角度
    print math.degrees(math.atan2(4, 3))
    print 4.0 / 3, math.sqrt(3)

    # 先得到弧度，然后根据角度和弧度转化公式得到角度
    print math.atan2(4, 3)
    print math.atan2(4, 3) * 180 / math.pi


if __name__ == '__main__':
    value_to_angel()

