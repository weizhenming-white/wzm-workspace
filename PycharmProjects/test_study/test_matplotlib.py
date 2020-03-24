#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-04-23 16:13
brief:练习matplotlib画图
"""

import matplotlib.pyplot as plt


x = [1, 3, 5, 7, 9]
y = range(len(x))

plt.plot(x, y)
plt.show()