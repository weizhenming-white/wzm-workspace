#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2019-04-22 16:58
brief:从ros bag里面提取数据
"""
from __future__ import print_function, division
from PIL import Image
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import rosbag
import sys
import os
import pylab as plt

# "/home/holo/bags/20200323/2020-03-23-10-47-38_hpp_2.bag", 
position_x_list = list()
position_y_list = list()
position_x_list2 = list()
position_y_list2 = list()
position_x_list3 = list()
position_y_list3 = list()
bag_name = ["/home/holo/bags/20200320/2020-03-20-16-03-05_hpp_2.bag", 
"/home/holo/bags/20200323/2020-03-23-11-04-13_hpp_2.bag", 
"/home/holo/bags/20200326/2020-03-26-10-43-18_route_2.bag"]
for rosbag_name in bag_name:
    bag = rosbag.Bag(rosbag_name)
    bag.read_messages()

    for topic, msg, t in bag.read_messages():
        if topic == "/holo/car_state_hpp":
            time_stamp = msg.header.stamp.secs
            position_x = msg.x
            position_y = msg.y
            speed_x = msg.vx
            speed_y = msg.vy
            heading = msg.heading
            gear_status = msg.gear_status
            take_over_request = msg.take_over_request

            # 行驶路径较好数据
            if rosbag_name is "/home/holo/bags/20200320/2020-03-20-16-03-05_hpp_2.bag":
                position_x_list.append(position_x)
                position_y_list.append(position_y)
            else:
                position_x_list2.append(position_x)
                position_y_list2.append(position_y)
        
        # 原始轨迹
        elif topic == "/holo/car_state":
            time_stamp = msg.header.stamp.secs
            position_x = msg.x
            position_y = msg.y
            speed_x = msg.vx
            speed_y = msg.vy
            heading = msg.heading
            gear_status = msg.gear_status
            take_over_request = msg.take_over_request

            position_x_list3.append(position_x)
            position_y_list3.append(position_y)
#         f.write(str(time_stamp) + "\t" + str(position_x) + "\t" + str(position_y) + "\t"
#                 + str(speed_x) + "\t" + str(speed_y) + "\t" + str(heading) + "\t"
#                 + str(gear_status) + "\t" + str(take_over_request) + "\n")
#
            print(time_stamp, "\t", position_x,
              "\t", position_y, "\t", speed_x, "\t",
              speed_y, "\t", heading, "\t", gear_status, "\t", take_over_request)

txt_name = "car_state.txt"
# f = open(txt_name, "a+")
#

plt.figure("trajectory graph")
plt.plot(position_x_list, position_y_list, 'b')
plt.plot(position_x_list2, position_y_list2, "r")
plt.plot(position_x_list3, position_y_list3, "y")
# plt.savefig('parking_trajectory_raw.jpg')
plt.show()
#
#         #print(position_x)
#         #print(msg)
#     # if topic == "/holo/control/control_command":
#     #     print(msg)
#     #     break
#
# # plt.plot(range(len(position_type)), position_type)
# # plt.show()
#
#
# print("finish!!!")
#
# f.close()
bag.close()