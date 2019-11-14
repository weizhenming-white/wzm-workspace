#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-04-25 14:40
brief:练习numpy库的常用方法
"""
import numpy as np


# 两个数组之间相加
def numpy_sum(n):
    """
    假设我们需要对两个向量 a 和 b 做加法。这里的向量即数学意义上的一维数组,随后我们将
    在第5章中学习如何用NumPy数组表示矩阵。向量 a 的取值为0~n的整数的平方,例如 n 取3时,向
    量 a 为0、1或4。向量 b 的取值为0~n的整数的立方,例如 n 取3时,向量 b 为0、1或8。
    """
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b

    return c


#将数据保存到文件里面
i2 = np.eye(2)
np.savetxt("save.txt", i2)




