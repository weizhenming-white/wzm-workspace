#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
time:2021-01-04 20:57
brief:按照指定的步数对图片进行抽帧，并保存抽完帧的图片
"""
import sys
sys.path.append('/home/holo/perception_data_filter')

import time
import third_libs.data_filter as data_filter
import os


def image_sampling(original_path, step, output_path):

    # 设置初始变量
    count = 0
    total = 0
    picture_path = []

    # 得到该目录下所有包含图片的目录
    for root, dirs, files in os.walk(original_path):
        for file in files:
            if os.path.splitext(file)[1] == '.jpeg':
                if root not in picture_path:
                    picture_path.append(root)
        for dir in dirs:
            image_sampling(dir, step, output_path)

    # 逐个过滤每个目录下的数据，按照指定的步数进行抽帧
    for i in picture_path:

        # 得到该目录下的图片数量
        tmp = int(os.popen('ls %s | grep jpeg | wc -l' % i).read())

        # 创建筛选之后的目录
        tmp_msg = i.split('/')[-4] + '/' + i.split('/')[-3] + '/' + i.split('/')[-2] + '/' + i.split('/')[-1]
        export_path = os.path.join(output_path, tmp_msg) # ex: output_path/2020-12-30-14-42-14/camera/front_right_h264/CAMERA_FRONT_RIGHT
        if not os.path.exists(export_path):
            os.makedirs(export_path)

        # 隔step抽一张
        count = 0
        for item in range(tmp):
            if (item == count) and count < tmp:
                old_name = os.path.join(i, str(item).zfill(8) + '.jpeg')
                new_name = os.path.join(export_path, str(item).zfill(8) + '.jpeg')
                print('copy %s to %s' % (old_name, new_name))
                os.system('cp %s %s' % (old_name, new_name))
                count += step


if __name__ == '__main__':

    # 设置初始变量
    original_path = '/media/holo/data1/wzm/test_data/birdview_image/zhonghaiguangchang/20201023'
    step = 10
    output_path = '/media/holo/data1/wzm/test_data/finally_image/birdview/zhonghaiguangchang/20201023'

    # 批量开始抽帧
    image_sampling(original_path, step, output_path)