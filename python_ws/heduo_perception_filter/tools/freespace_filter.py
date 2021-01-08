#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
time:2021-01-05 10:39
brief:过滤空洞和距离较近的障碍物，拿到时间戳，进行相机匹配
"""

import sys
sys.path.append('/home/holo/perception_data_filter')

import rosbag
import rospy
import sys
import os
import math
import time
import third_libs.data_filter as data_filter


def read_bag(bag_name, topic_list):

    # 设置初始变量
    timestamp_data = {}
    vehicle_info_start_time = 0
    freespace_start_time = 0
    offset = 0
    vehicle_info_count = 0
    freespace_count = 0
    image_data = {}

    # 读取bag
    bag = rosbag.Bag(bag_name)
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):

        if topic == '/holo/gateway/vehicle_info_weltmeister':

            # 读取每一帧的时间
            secs = float(msg.header.stamp.secs)
            nsec = float(msg.header.stamp.nsecs) / 1000000000
            stamp = float("%.2f" % (secs + nsec))

            # 将第一帧的时间戳赋值给vehicle_info_start_time
            if vehicle_info_count == 0:
                vehicle_info_start_time = stamp
                vehicle_info_count += 1

        # 设置循环内初始变量
        tag_list = []

        # 过滤freespace数据
        if topic == '/holo/perception/vision/parking_freespace':

            # 读取每一帧的时间
            secs2 = float(msg.header.stamp.secs)
            nsec2 = float(msg.header.stamp.nsecs) / 1000000000
            stamp2 = float("%.2f" % (secs2 + nsec2))

            # 将第一帧的时间戳赋值给freespace_start_time
            if freespace_count == 0:
                freespace_start_time = stamp2
                freespace_count += 1

            # 循环每个freespace的数据
            for i in range(len(msg.obstacles)):
                x = float(msg.obstacles[i].position.x)
                y = float(msg.obstacles[i].position.y)

                # 判断当前这条数据的类型是否为空洞
                if int(msg.obstacles[i].classification) == 1:

                    # 判断当前点是在哪个象限（车体坐标系为:x朝左为正，y朝上为正）
                    # 判断当前点是否在第一象限，如在，则添加标志位1,3,5
                    if (x >= 0) and (y >= 0):
                        if 'CAMERA_FRONT_CENTER_GS' not in tag_list:
                            tag_list.append('CAMERA_FRONT_CENTER_GS')
                        if 'CAMERA_FRONT_LEFT' not in tag_list:
                            tag_list.append('CAMERA_FRONT_LEFT')
                        if 'CAMERA_FRONT_CENTER' not in tag_list:
                            tag_list.append('CAMERA_FRONT_CENTER')

                    # 判断当前点是否在第二象限，如在，则添加标志位1,4,5
                    if (x >= 0) and (y <= 0):
                        if 'CAMERA_FRONT_CENTER_GS' not in tag_list:
                            tag_list.append('CAMERA_FRONT_CENTER_GS')
                        if 'CAMERA_FRONT_RIGHT' not in tag_list:
                            tag_list.append('CAMERA_FRONT_RIGHT')
                        if 'CAMERA_FRONT_CENTER' not in tag_list:
                            tag_list.append('CAMERA_FRONT_CENTER')

                    # 判断当前点是否在第三象限，如在，则添加标志位2,4
                    if (x <= 0) and (y <= 0):
                        if 'CAMERA_REAR_CENTER' not in tag_list:
                            tag_list.append('CAMERA_REAR_CENTER')
                        if 'CAMERA_FRONT_RIGHT' not in tag_list:
                            tag_list.append('CAMERA_FRONT_RIGHT')

                    # 判断当前点是否在第四象限，如在，则添加标志位2,3
                    if (x <= 0) and (y >= 0):
                        if 'CAMERA_REAR_CENTER' not in tag_list:
                            tag_list.append('CAMERA_REAR_CENTER')
                        if 'CAMERA_FRONT_LEFT' not in tag_list:
                            tag_list.append('CAMERA_FRONT_LEFT')

            # 判断这一帧数据是否有空洞，如果有则将时间戳添加进列表里,并过滤掉其他重复的时间戳
            if len(tag_list) > 0:
                if len(timestamp_data.keys()) == 0:
                    timestamp_data[secs2] = tag_list
                else:
                    if secs2 != timestamp_data.keys()[-1]:
                        timestamp_data[secs2] = tag_list

        # 计算两个topic第一帧时间戳的偏差量，并赋值给offset
        if vehicle_info_count != 0 and freespace_count != 0:
            offset = freespace_start_time - vehicle_info_start_time

    # 关掉bag
    bag.close()

    # 将freespace的时间戳转化成图像导出来的时间戳
    for i in timestamp_data.keys():
        image_data[int(i - offset)] = timestamp_data[i]

    return image_data


# print read_bag('/home/holo/bags/sport_bag/20201230/2020-12-30-14-20-48.bag', ['/holo/perception/vision/parking_freespace', '/holo/gateway/vehicle_info_weltmeister'])


def get_target_image(image_path, data, output_path):

    # 批次处理一个bag的所有图片
    for i in image_path:
        print "analysis", i

        # 将需要导出的数据编号记录到列表里面
        output_num = []

        # 将过滤后的数据编号添加到新的列表里面
        export_num = []

        # 创建导出变量
        export_path = ''

        # 读取timestamp.txt的时间戳
        with open('%s' % os.path.join(i, 'timestamps.txt')) as f:
            for line in f:
                tmp_stamp = int(float(line.split()[1]))
                if tmp_stamp in data.keys():
                    if os.path.split(i)[1] in data[tmp_stamp]:
                        output_num.append(line.split()[0])

        # 创建需要导出的目录
        if len(output_num) > 0:
            tmp_msg = i.split('/')[-4] + '/' + i.split('/')[-3] + '/' + i.split('/')[-2] + '/' + i.split('/')[-1]
            export_path = os.path.join(output_path, tmp_msg)
            if not os.path.exists(export_path):
                os.makedirs(export_path)

        # 将得到的数据隔三张抽一张
        count = 0
        step = 3
        for item in range(len(output_num)):
            if (item == count) and count < len(output_num):
                export_num.append(output_num[item])
                count += step

        # 开始将过滤之后的数据导出来
        for num in export_num:
            old_name = os.path.join(i, str(num).zfill(8) + '.jpeg')
            new_name = os.path.join(export_path, str(num).zfill(8) + '.jpeg')
            os.system('cp %s %s' % (old_name, new_name))
            print('copy %s to %s' % (old_name, new_name))


if __name__ == '__main__':

    # 设置初始变量
    topic_list = ['/holo/perception/vision/parking_freespace', '/holo/gateway/vehicle_info_weltmeister']
    original_path = '/media/holo/data1/wzm/test_data/sport_bag/bimuyu/20210106'              # bag目录
    original_image_path = '/media/holo/data1/wzm/test_data/raw_image/bimuyu/20210106'            # 图像目录
    output_path = '/media/holo/data1/wzm/test_data/filter_image/bimuyu/20210106'

    # 得到所有的bag绝对路径
    bag_data = data_filter.bianli(original_path, '.bag')

    # 将所有包含图片的目录赋值给image_path
    image_path_all = data_filter.bianli_folder(original_image_path, '.jpeg')

    # 批量导出该目录下的所有
    for bag in bag_data:

        timestamp_data = read_bag(bag, topic_list)

        # 过滤bag名字，并将bag名字赋值给target_msg
        target_msg = os.path.splitext(os.path.basename(bag))[0]  # ex: 2020-12-31-09-01-57
        print target_msg

        # 得到当前bag所对应的目录
        image_path = []
        for i in image_path_all:
            if target_msg in i:
                image_path.append(i)

        # 开始执行过滤函数
        get_target_image(image_path, timestamp_data, output_path)
