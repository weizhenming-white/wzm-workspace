#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
time:2021-01-06 16:14
brief:将所有的数据归整到一个主目录下面，并按照顺序依次命名
"""

import os


def move_file(path, output_path):
    """
    批量修改文件名，按照指定序号,并将目录相同的图片归整到一起
    :param path: 要处理的图片路径
    :param output_path: 处理后的路径存放位置
    :return:
    """

    # 设置初始变量
    front_wide = 0
    front_sv = 0
    rear_sv = 0
    left_sv = 0
    right_sv = 0

    # 将所有的数据整理到以五个相机命名的目录下
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_CENTER':
                export_front_wide = os.path.join(output_path, 'CAMERA_FRONT_CENTER/')
                if not os.path.exists(export_front_wide):
                    os.makedirs(export_front_wide)
                os.system('cp %s %s' % (file_path, os.path.join(export_front_wide, str(front_wide).zfill(8) + '.jpeg')))
                front_wide += 1
                print('rename front wide ...................................................')
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_CENTER_GS':
                export_front_sv = os.path.join(output_path, 'CAMERA_FRONT_CENTER_GS/')
                if not os.path.exists(export_front_sv):
                    os.makedirs(export_front_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_front_sv, str(front_sv).zfill(8) + '.jpeg')))
                front_sv += 1
                print('rename front sv ...................................................')
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_LEFT':
                export_left_sv = os.path.join(output_path, 'CAMERA_FRONT_LEFT/')
                if not os.path.exists(export_left_sv):
                    os.makedirs(export_left_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_left_sv, str(left_sv).zfill(8) + '.jpeg')))
                left_sv += 1
                print('rename left sv ...................................................')
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_RIGHT':
                export_right_sv = os.path.join(output_path, 'CAMERA_FRONT_RIGHT/')
                if not os.path.exists(export_right_sv):
                    os.makedirs(export_right_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_right_sv, str(right_sv).zfill(8) + '.jpeg')))
                right_sv += 1
                print('rename right sv ...................................................')
            if str(file_path.split('/')[-2]) == 'CAMERA_REAR_CENTER':
                export_rear_sv = os.path.join(output_path, 'CAMERA_REAR_CENTER/')
                if not os.path.exists(export_rear_sv):
                    os.makedirs(export_rear_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_rear_sv, str(rear_sv).zfill(8) + '.jpeg')))
                rear_sv += 1
                print('rename rear sv ...................................................')
        for dir in dirs:
            move_file(dir, output_path)


if __name__ == '__main__':

    # 设置初始变量
    original_path = '/media/holo/data1/wzm/test_data/sampling_image/detection/bimuyu/20210106'
    output_path = '/media/holo/data1/wzm/test_data/finally_image/detection_sampling/bimuyu/20210106'

    # 调用函数批量归纳数据
    move_file(original_path, output_path)