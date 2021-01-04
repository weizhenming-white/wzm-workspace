#!/usr/bin/env python
# -*- coding:utf-8 -*-

import rosbag
from functools import reduce
from itertools import islice
import time
import third_libs.data_filter as data_filter
import os


def one():
    """
    测试输出效果
    :return:
    """
    print("111111111111111")


def test_bag():
    bag_name = '/media/holo/data1/workspace_test/bags/20201030_oulu/2020-10-30-17-56-02_hpp_304.bag'
    topic_list = ['/holo/gateway/vehicle_info_weltmeister',
                  '/holo/perception/vision/parking_freespace',
                  '/holo/sensors/camera/front_center_h264']
    count = 0
    offset = 0
    tmp_list = []
    zero_timestamp_list_tmp = []
    start_time = 0

    bag = rosbag.Bag(bag_name)
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):
        if topic == '/holo/gateway/vehicle_info_weltmeister':
            # print(msg)
            secs = float(msg.header.stamp.secs)
            nsec = float(msg.header.stamp.nsecs) / 1000000000
            stamp = float("%.2f" % (secs + nsec))
            speed = float(msg.vehicle_speed)
            if count == 0:
                start_time = float(str(timestamp)[0:10] + '.' + str(timestamp)[10:12])
                print('The bag start time is : %s' % (str(timestamp)[0:10] + '.' + str(timestamp)[10:12]))
                print("The /holo/gateway/vehicle_info_weltmeister start time is : %s" % str(stamp))
                offset = float(str(timestamp)[0:10] + '.' + str(timestamp)[10:12]) - stamp
                print('The deviation is : %s' % str(offset))
            count += 1
            if speed > 0:
                # print(stamp)
                if int(secs) not in tmp_list:
                    tmp_list.append(int(secs))

            # print(timestamp)

        """
        if topic == '/holo/perception/vision/parking_freespace':
            # print(msg)
            # print(timestamp)
            secs = float(msg.obstacles[0].header.stamp.secs)
            nsec = float(msg.obstacles[0].header.stamp.nsecs) / 1000000000
            stamp = float("%.2f" % (secs + nsec))
            # print("/holo/perception/vision/parking_freespace timestamp is ", stamp)
        if topic == '/holo/sensors/camera/front_center_h264':
            # print(msg)1604051861
            # print(timestamp)
            # break
            pass
        """
    bag.close()
    # print(tmp_list)
    for i in tmp_list:
        zero_timestamp_list_tmp.append(i + offset)
    # print(zero_timestamp_list_tmp)

    # 获取列表中连续的数字
    def divide(value, element):
        if not value[-1] or element - value[-1][-1] == 1:
            value[-1].append(element)
        else:
            value.append([element])

        return value

    slices = [(array[0], array[-1]) for array in reduce(divide, zero_timestamp_list_tmp, [[]])]

    # print(slices)
    print('\n\nThis bag has %d parts. Start beginning..........................' % len(slices))
    tmp_num = 1
    output_path = '/home/holo/bags/test'
    for start, end in slices:
        start_dt = data_filter.TimestampConversion(start, 0)
        end_dt = data_filter.TimestampConversion(end, 0)
        new_name = os.path.join(output_path, str(start_dt) + '.bag')
        # os.system('rosbag filter %s %s "(t.to_sec() >= %.1f and t.to_sec() <= %.1f)"' % (bag_name, new_name, start, end))
        print(start, end)
        print(int(start), int(end))
        print(start_dt, end_dt)


def test_rosbag():
    """

    :return:
    """
    os.system('rosbag play /home/holo/bags/test/2020-10-30-17-56-09.bag')


if __name__ == '__main__':
    test_bag()
