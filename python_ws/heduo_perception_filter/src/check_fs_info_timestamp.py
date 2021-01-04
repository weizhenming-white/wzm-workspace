#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-20 20:18
brief: 比较freespace和vehicle info时间戳的差异，找出规律
"""

import rosbag
import sys
import os
import math
import time


def check_timestamp(bag_path, topic_list):
    freespace_timestamp = []
    vehicle_info = []

    bag = rosbag.Bag(bag_path)
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):
        if topic == '/holo/perception/vision/parking_freespace':
            secs = float(msg.header.stamp.secs)
            nsec = float(msg.header.stamp.nsecs) / 1000000000
            stamp = secs + nsec
            if len(freespace_timestamp) == 0:
                freespace_timestamp.append(secs)
            else:
                if secs != freespace_timestamp[-1]:
                    freespace_timestamp.append(secs)
        if topic == '/holo/gateway/vehicle_info_weltmeister':
            secs2 = float(msg.header.stamp.secs)
            nsec2 = float(msg.header.stamp.nsecs) / 1000000000
            stamp2 = secs2 + nsec2
            if len(vehicle_info) == 0:
                vehicle_info.append(secs2)
            else:
                if secs2 != vehicle_info[-1]:
                    vehicle_info.append(secs2)

    print("freespace timestamp length is ", len(freespace_timestamp))
    print('==========================================================')
    print(freespace_timestamp)
    freespace_timestamp_tmp = []
    for i in freespace_timestamp:
        time_local = time.localtime(i)
        dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
        # print(dt)
        # print(freespace_timestamp.index(i))
        freespace_timestamp_tmp.append(dt)
    print(freespace_timestamp_tmp)
    print('==========================================================\n\n')
    print("vehicle info timestamp length is ", len(vehicle_info))
    print('==========================================================')
    print(vehicle_info)
    vehicle_info_tmp = []
    for i in vehicle_info:
        time_local = time.localtime(i)
        dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
        # print("vehicle info timestamp: ", dt)
        vehicle_info_tmp.append(dt)
    print(vehicle_info_tmp)
    print('==========================================================\n\n')

    print('freespace and vehicle_info timestamp differ : %.3f' % (freespace_timestamp[0] - vehicle_info[0]))


if __name__ == '__main__':
    # bag_path = '/home/holo/bags/20201113/2020-11-13-11-23-45_route_31.bag'   # 差315964783.000
    # bag_path = '/home/holo/bags/20201110/2020-11-10-17-39-28_route_15.bag'      # 差315964782.000
    bag_path = '/home/holo/bags/20201110/2020-11-10-16-40-37_fs.bag'               # 差315964782.000
    # bag_path = '/home/holo/bags/20201110/2020-11-10-17-43-11_hpp_15.bag'            # 差315964782.000
    topic_list = ['/holo/perception/vision/parking_freespace', '/holo/gateway/vehicle_info_weltmeister']
    check_timestamp(bag_path, topic_list)