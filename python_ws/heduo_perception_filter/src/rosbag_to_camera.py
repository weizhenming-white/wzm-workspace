#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-12-16 14:58
brief:解析TDA4上记录的数据，并转化成图片
"""

import rosbag
import sys
import os
import math
import time
import cv2
import numpy as np


def read_bag(bag_path, topic_list):
    # 初始化ros类
    bag = rosbag.Bag(bag_path)

    # 读取bag信息
    tmp_frame = open('tmp_frame.txt', 'w')
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):
        if topic == '/holo/sensors/camera/front_center_encoder':
            # data = np.reshape(msg, (1280, 960))
            # print msg
            str1 = str(msg).split(':')[1].lstrip()
            str2 = str1.replace('[', '').replace(']', '')
            list_tmp = str2.split(',')
            print list_tmp
            print type(list_tmp)
            print len(list_tmp)
            tmp_frame.write(str(list_tmp))
            # cv2.imshow("src", msg)
            break

    tmp_frame.close()
    bag.close()



if __name__ == '__main__':
    bag_path = '/home/holo/bags/20201216/2020-12-16-13-42-18_TDA4.bag'
    topic_list = ['/holo/sensors/camera/front_center_encoder', '/holo/sensors/camera/front_left_encoder']
    read_bag(bag_path, topic_list)