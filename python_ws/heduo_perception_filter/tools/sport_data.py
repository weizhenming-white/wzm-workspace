#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
time:2021-01-04 17:56
brief:将rosbag里面的静态数据去除，重新生成新的bag
"""
import sys
sys.path.append('/home/holo/perception_data_filter')

import rosbag
from functools import reduce
from itertools import islice
import time
import third_libs.data_filter as data_filter
import os


def get_sport_timestamp(bag_name):

    # 设置初始量
    count = 0
    offset = 0
    tmp_list = []
    zero_timestamp_list_tmp = []
    start_time = 0

    # 读取bag
    bag = rosbag.Bag(bag_name)
    for topic, msg, timestamp in bag.read_messages(topics='/holo/gateway/vehicle_info_weltmeister'):

        # 读取每一帧的时间
        secs = float(msg.header.stamp.secs)
        nsec = float(msg.header.stamp.nsecs) / 1000000000
        stamp = float("%.2f" % (secs + nsec))

        # 获得当前帧的速度
        speed = float(msg.vehicle_speed)

        # 得到第一帧的rosbag时间，vehicle_info的第一帧时间，并计算两个时间的偏差量
        if count == 0:
            start_time = float(str(timestamp)[0:10] + '.' + str(timestamp)[10:12])
            print('The bag start time is : %s' % (str(timestamp)[0:10] + '.' + str(timestamp)[10:12]))
            print("The /holo/gateway/vehicle_info_weltmeister start time is : %s" % str(stamp))
            offset = float(str(timestamp)[0:10] + '.' + str(timestamp)[10:12]) - stamp
            print('The deviation is : %s' % str(offset))
        count += 1

        # 当速度>0时，将vehicle_info当前帧的时间加入到列表里面
        if speed > 0:
            # print(stamp)
            if int(secs) not in tmp_list:
                tmp_list.append(int(secs))

    # 关掉bag
    bag.close()

    # 将列表里面的vehicle_info时间转换成系统时间
    for i in tmp_list:
        zero_timestamp_list_tmp.append(i + offset)

    # 获取列表中连续的数字,ex:[(1604051769.13, 1604051844.13), (1604051847.13, 1604051861.13)]
    def divide(value, element):
        if not value[-1] or element - value[-1][-1] == 1:
            value[-1].append(element)
        else:
            value.append([element])
        return value
    try:
        slices = [(array[0], array[-1]) for array in reduce(divide, zero_timestamp_list_tmp, [[]])]
    except Exception as e:
        print("Error: ", e)
        slices = []

    return slices


def get_new_bag(bag_name, data, output_path):

    # 显示需要过滤的总数量
    print('\n\nThis bag has %d parts. Start beginning..........................' % len(data))

    # 设置计数变量
    tmp_num = 0

    # 重新生成新的bag
    if len(data) > 0:
        for start, end in data:

            # 将开始时间戳转化成时间专用格式
            start_dt = data_filter.TimestampConversion(start, 0)

            # 得到新的bag名字
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            new_name = os.path.join(output_path, str(start_dt) + '.bag')

            # 显示正在处理的bag名字
            tmp_num += 1
            print('Progress: [%d / %d]' % (tmp_num, len(data)))

            # 开始过滤所需要时间段的bag数据
            os.system(
                'rosbag filter %s %s "(t.to_sec() >= %.1f and t.to_sec() <= %.1f)"' % (bag_name, new_name, start, end))
        os.system('rm -f %s' % bag_name)


if __name__ == '__main__':

    # 设置初始变量
    original_path = '/home/holo/bags/20210107'
    output_path = '/home/holo/bags/sport_bag/bimuyu/20210107'

    # 得到所有的bag绝对路径
    data = data_filter.bianli(original_path, '.bag')

    # 批量导出该目录下的所有动态数据
    for bag in data:
        timestamp_data = get_sport_timestamp(bag)
        get_new_bag(bag, timestamp_data, output_path)
