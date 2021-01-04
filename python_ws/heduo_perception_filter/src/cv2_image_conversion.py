#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-26 14:15
brief: opencv将灰度图转换成RGB
"""


from __future__ import division
import numpy as np
import cv2

src = cv2.imread("/home/holo/Pictures/Case1.png")
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# RGB在opencv中存储为BGR的顺序,数据结构为一个3D的numpy.array,索引的顺序是行,列,通道:
B = src[:, :, 0]
G = src[:, :, 1]
R = src[:, :, 2]
# 灰度g=p*R+q*G+t*B（其中p=0.2989,q=0.5870,t=0.1140），于是B=(g-p*R-q*G)/t。于是我们只要保留R和G两个颜色分量，再加上灰度图g，就可以回复原来的RGB图像。
g = src_gray[:]
p = 0.2989; q = 0.5870; t = 0.1140
B_new = (g - p * R - q * G) / t
B_new = np.uint8(B_new)
src_new = np.zeros((src.shape)).astype("uint8")
src_new[:, :, 0] = B_new
src_new[:, :, 1] = G
src_new[:, :, 2] = R
# 显示图像
cv2.imshow("input", src)
cv2.imshow("output", src_gray)
cv2.imshow("result", src_new)
cv2.waitKey(0)
cv2.destroyAllWindows()