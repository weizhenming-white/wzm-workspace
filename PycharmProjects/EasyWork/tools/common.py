#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-07-06 20:28
brief:存放一些常用的工具脚本（如：已知两点坐标，求距离；直角三角形，已知两边，求第三边）
"""

def distance(A, B):
    """
    求两点距离
    """
    tmp = pow((A[0] - B[0]), 2) + pow((A[1] - B[1]), 2)
    distan = pow(tmp, (1.0 / 2))
    return distan

def length(x):
    """
    直角三角形，知道两个直角边，求第三边
    """
    length = pow(pow(x, 2) * 2, (1.0 / 2))
    return length





if __name__ == "__main__":
    # dis = distance([0, 0], [1, 1])
    # print dis
    print length(3)