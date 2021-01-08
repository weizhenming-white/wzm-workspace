#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-12-22 20:16
brief: 通用方法库
    1. bianli() : 遍历指定的文件目录和文件类型
    2. sampling() : 对图片进行采样，按照指定的步伐进行采样
    3.
"""

import os
import sys
import time


def bianli(path, params):
    """
    遍历指定文件的数量
    :param path: 需要过滤的文件夹
    :param params: 需要过滤的文件类型。如'.jpg','.bag'
    :return: 返回带有这个文件的绝对路径的列表，以及数量
    """

    count = 0
    data = []

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            if os.path.splitext(file)[1] == params:
                count += 1
                data.append(file_path)

        for dir in dirs:
            pass
            # bianli(dir, params)

    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print("=============================================================================================")

    return data


def bianli_folder(path, params):
    """
    遍历指定目录，得到该目录下所有包含params后缀的子目录
    :param path: 目标路径
    :param params: 需要过滤的文件类型。如'.jpg','.bag'
    :return: 返回带有这个文件的子目录的绝对路径，以及数量
    """

    # 设置初始变量
    count = 0
    data = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == params:
                if root not in data:
                    data.append(root)
                    count += 1
        for dir in dirs:
            bianli_folder(dir, params)

    # 打印所需要数据的数量信息
    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print("=============================================================================================")

    return data


def sampling(path, step):
    """
    对数据进行采样，间隔step张图片抽一张
    :param path: 传入的路径
    :param step: 步长，间隔多少张采集一张
    :return:
    """
    pass


def TimestampConversion(value, params):
    """
    时间戳转化函数
    :param value: 时间戳 or 系统时间
    :param params: 0-代表将时间戳转化成系统时间；1-代表将系统时间转化成时间戳
    :return: 系统时间 or 时间戳
    """
    if params == 0:
        time_local = time.localtime(int(value))
        dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
        return dt
