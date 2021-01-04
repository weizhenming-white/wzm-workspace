#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-09-02 19:36
brief:过滤出freespace的bad case，并自动化导出成图片
"""

import rosbag
import sys
import os

path = "/home/holo/bags/20201109/2020-11-09-15-22-07_route_14.bag"
path_list = ["/home/holo/bags/freespace/one/2020-10-27-14-52-00_hpp_30.bag"]
topic_name = ["/holo/perception/vision/parking_freespace", ]


def process(path):
    bag = rosbag.Bag(path)
    # freespace = open("output/freespace_tmp.txt", "w")
    time_list = list()              # 记录每次出现空洞的时间戳

    for topic, msg, timestamp in bag.read_messages(topics="/holo/perception/vision/parking_freespace"):
        # freespace.write(str(msg.obstacles))
        if len(msg.obstacles) > 10:                     # 当障碍物数量大于10时，默认出现空洞
            if len(time_list) < 1:
                time_list.append(int(msg.obstacles[10].header.stamp.secs))
            else:
                if int(msg.obstacles[10].header.stamp.secs) > time_list[-1] + 10:           # 空洞与空洞之间的间隔为10s
                    time_list.append(int(msg.obstacles[10].header.stamp.secs))

            print "This time is ", msg.obstacles[10].header.stamp.secs, timestamp
            print "obstacles list is ", len(msg.obstacles)
            print "obstacle classification is ", msg.obstacles[10].classification

    print "========================================="
    print
    print "This bag split points", time_list
    bag.close()
    # freespace.close()

    bag_list = list()
    # 基于空洞时间分段切割bag
    for i in time_list:
        bag_list.append(os.path.join(os.getcwd(), 'output/out%s.bag' % str(i)))
        os.system('rosbag filter %s output/out%s.bag '
                  '"t.to_sec() >= %s and t.to_sec() <= %s"' % (path, str(i), str(i - 10), str(i + 10)))
    return bag_list


def get_takeover(path):
    bag = rosbag.Bag(path)
    for topic, msg, timestamp in bag.read_messages(topics=""):
        pass
    bag.close()


def get_picture():
    bag_list = process(path)

    # 调试，直接给出路径，通过路径过滤后缀名为“.bag”的文件
    # bag_list = list()
    # for root, dirs, files in os.walk(os.getcwd() + '/' + 'output'):
    #     for file in files:
    #         if os.path.splitext(file)[1] == '.bag':
    #             print "add........................."
    #             bag_list.append(os.path.join(root, file))
    print bag_list
    output_path = os.getcwd() + '/' + 'picture'
    print output_path
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print "===========Create folder name is picture===================="

    for i in bag_list:
        file_name = os.path.split(i)[1]
        export_path = os.path.splitext(file_name)[0]
        os.system('/home/holo/workspace/hpp_20201104/target/bin/ros/export_3d_data_cmw '
                  '-i %s --camera_yaml_path '
                  '/home/holo/workspace/hpp_20201104/target/config/holo_data_provider/app_config/camera.yaml '
                  '-o %s --output_camera_image 1' % (i, output_path + '/' + export_path))


if __name__ == '__main__':
    RootPath = '/home/holo/workspace/wzm-workspace/PycharmProjects/EasyWork/tools/output'
    # for i in path_list:
    #     process(i)
    # bianli(RootPath)

    """     测试os模块
    path = "/home/holo/workspace/wzm-workspace/PycharmProjects/EasyWork/" \
           "tools/output/picture/out1604383080/camera/front_right_h264/CAMERA_FRONT_RIGHT/00000075.jpeg"
    (file_path, filename) = os.path.split(path)                                                              
    print os.path.splitext(filename)[1]
    if os.path.splitext(path)[1] == '.jpeg':
        print "1"
    print
    """

    # get_picture()

    # bianli('/home/holo/perception_data_filter/picture')



