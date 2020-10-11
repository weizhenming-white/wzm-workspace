#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-02 19:36
brief:处理rosbag，并可视化
"""

import rosbag
import sys

path = "/home/holo/workspace_sim/hpp_sim_test/hpp/target/route_7/2020-09-02-19-37-15-route_7.bag"


def process(path):
    odo_position_list = [[], [], []]
    odo_xy_position_list = []
    bag = rosbag.Bag(path)
    bag.read_messages()
    for topic, msg, timestamp in bag.read_messages(topics="/vehicle_odometry_hpp"):
        odo_position_list[0].append(float(msg.pose.position.x))  # x
        odo_position_list[1].append(float(msg.pose.position.y))  # y
        odo_position_list[2].append(float(msg.pose.position.z))  # z
        odo_xy_position_list.append([float(msg.pose.position.x), float(msg.pose.position.y)])
        print "x = %f, y = %f, z = %f" % (float(msg.pose.position.x), float(msg.pose.position.y), float(msg.pose.position.z))


if __name__ == '__main__':
    ms = sys.path
    print ms
    process(path)



