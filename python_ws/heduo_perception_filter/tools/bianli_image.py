#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
time:2021-01-06 17:18
brief:遍历目录下所有的image数量，并分别统计不同的相机数量
"""
import os
import sys


def bianli(path, params):

    # 设置参数
    count = 0
    front_wide_count = 0
    front_sv_count = 0
    left_sv_count = 0
    right_sv_count = 0
    rear_sv_count = 0

    # 开始遍历统计
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # 过滤出后缀名为'.jpeg'的文件，并统计
            if os.path.splitext(file)[1] == params:
                print(file_path)
                count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_CENTER':
                    front_wide_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_CENTER_GS':
                    front_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_LEFT':
                    left_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_RIGHT':
                    right_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_REAR_CENTER':
                    rear_sv_count += 1

        for dir in dirs:
            bianli(dir, params)
    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print('The front wide number is %d' % front_wide_count)
    print('The front sv number is %d' % front_sv_count)
    print('The left sv number is %d' % left_sv_count)
    print('The right sv number is %d' % right_sv_count)
    print('The rear sv number is %d' % rear_sv_count)
    print("=============================================================================================")


if __name__ == '__main__':

    bianli(sys.argv[1], sys.argv[2])