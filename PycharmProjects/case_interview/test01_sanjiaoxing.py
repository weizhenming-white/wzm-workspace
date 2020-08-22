#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author:魏振明
time:2020-06-29 17:39
brief:输入三个数字，确定这三个数字能组成什么三角形
"""


def parseTrigon(a, b, c):
    """
    -1代表输入值的类型不对
    0代表三个值无法构成三角形
    1代表普通三角形
    2代表等腰三角形
    3代表等边三角形
    """
    data = [a, b, c]
    for i in data:
        if 1 <= i <= 10:
            pass
        else:
            return -1                 # 不是int类型或不是数字
    for i in data:
        if ((a + b) <= c) or ((a + c) <= b) or ((b + c) <= a):
            return 0                       # 两边之和小于或等于第三边
        if (a != b) and (a != c) and (b != c):
            return 1                  # 普通三角形
        if a == b == c:
            return 3                    # 等边三角形
        if (a == b) or (a == c) or (b == c):
            return 2                    # 等腰三角形


if __name__ == "__main__":
    print(parseTrigon(3, 3, 6))