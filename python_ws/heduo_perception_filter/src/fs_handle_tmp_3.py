#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-12-09 19:17
brief:同时考虑距离和空洞，缩小过滤的距离为车身周围1m的障碍物，主要过滤空洞
"""

import rosbag
import rospy
import sys
import os
import math
import time

topic_dict = {1: '/holo/sensors/camera/front_center_gs_h264',
              2: '/holo/sensors/camera/rear_center_h264',
              3: '/holo/sensors/camera/front_left_h264',
              4: '/holo/sensors/camera/front_right_h264',
              5: '/holo/sensors/camera/front_center_h264'}
yaml_file_dict = {1: 'front_center_camera_ov490.yaml',
                  2: 'rear_center_camera_ov490.yaml',
                  3: 'left_center_camera_ov490.yaml',
                  4: 'right_center_camera_ov490.yaml',
                  5: 'front_center_camera_ar.yaml'}


def read_bag(bag_path, topic_list):
    # 设置变量
    bag = rosbag.Bag(bag_path)
    time_list = []
    time_data = {}
    msgs = 0
    start_time = 0

    # tmp_txt = open('output/tmp.txt', 'w')
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):

        tag_list = []
        if topic == '/holo/perception/vision/parking_freespace':
            if msgs == 0:
                start_time = float(msg.header.stamp.secs)
            msgs += 1

            # 确定obstacles list
            # print(len(msg.obstacles))
            # count = count + 1
            # print('\n', count)

            # 显示freespace的类型，通过观察classification得到。
            # 暂时有三个类型（0-range，2-freespace，1-nofreespace）----通过数据分析的，不一定准确
            count = 0
            for i in range(len(msg.obstacles)):
                x = float(msg.obstacles[i].position.x)
                y = float(msg.obstacles[i].position.y)
                distan = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
                # print('x：%f\t\ty：%f' % (x, y))
                # print('Distance：%.6f' % distan)

                # 基于车身前后1m, 左右0.5m范围进行过滤，或者是空洞的话，如存在，则将tag置为1
                if ((-1.934 <= x <= 4.65) and (-1.417 <= y <= 1.417)) or int(msg.obstacles[i].classification) == 1:

                    print(x, y)

                    # 判断当前点是否在第一象限，如在，则添加标志位1,3,5
                    if (x >= 0) and (y >= 0):
                        if 1 not in tag_list:
                            tag_list.append(1)
                        if 3 not in tag_list:
                            tag_list.append(3)
                        if 5 not in tag_list:
                            tag_list.append(5)

                    # 判断当前点是否在第二象限，如在，则添加标志位1,4,5
                    if (x >= 0) and (y <= 0):
                        if 1 not in tag_list:
                            tag_list.append(1)
                        if 4 not in tag_list:
                            tag_list.append(4)
                        if 5 not in tag_list:
                            tag_list.append(5)

                    # 判断当前点是否在第三象限，如在，则添加标志位2,4
                    if (x <= 0) and (y <= 0):
                        if 2 not in tag_list:
                            tag_list.append(2)
                        if 4 not in tag_list:
                            tag_list.append(4)

                    # 判断当前点是否在第四象限，如在，则添加标志位2,3
                    if (x <= 0) and (y >= 0):
                        if 2 not in tag_list:
                            tag_list.append(2)
                        if 3 not in tag_list:
                            tag_list.append(3)

                    # print("This bad case distance is %.6f" % distan)

                    # tmp_txt.write('x：%f\t\ty：%f\n' % (x, y) + 'Distance：%.6f\n' % distan)

                # 获取时间戳，精确到小数点后6位
                # secs = float(msg.obstacles[i].header.stamp.secs)
                # nsec = float(msg.obstacles[i].header.stamp.nsecs) / 1000000000
                # nsec = msg.obstacles[i].header.stamp.nsecs
                # stamp = secs + nsec
                # print('%.6f' % stamp)

                # 判断障碍物类型为no-freespace时，统计这一帧的no-freespace数量
                # elif int(msg.obstacles[i].classification) == 1:
                #     count = count + 1

            # 将出现空洞那一帧的时间戳添加到list里面
            # if count > 0:
            # print('\n==============================\n')
            # print(tag_list)
            secs = float(msg.header.stamp.secs)
            nsec = float(msg.header.stamp.nsecs) / 1000000000
            stamp = secs + nsec
            topic_filter = []
            yaml_filter = []
            if len(tag_list) > 0:

                if len(time_list) == 0:
                    print('Add timestamp to list')

                    # 得到需要导出的topic组成的yaml
                    for i in range(len(tag_list)):
                        topic_filter.append(topic_dict[tag_list[i]])
                        yaml_filter.append(yaml_file_dict[tag_list[i]])
                    time_list.append(secs)
                    time_data[secs] = "topic: %s\nyaml_file: %s" % (str(topic_filter), str(yaml_filter))
                else:
                    if secs != time_list[-1]:
                        for i in range(len(tag_list)):
                            topic_filter.append(topic_dict[tag_list[i]])
                            yaml_filter.append(yaml_file_dict[tag_list[i]])
                        # print(topic_filter, yaml_filter)
                        time_list.append(secs)
                        time_data[secs] = "topic: %s\nyaml_file: %s" % (str(topic_filter), str(yaml_filter))

            # print('no-freespace number is: ', count)

            # tmp_txt.write('\n==============================\n'
            #               + 'no-freespace number is: %d\n' % count
            #               + "This frame list count is %d\n" % len(msg.obstacles))

    # tmp_txt.write('\n\n' + str(time_list))
    # tmp_txt.close()
    # print(time_list)
    bag.close()
    print(time_list)
    print(time_data)
    print('start time is ', start_time)
    print("%s has %d bad case." % (bag_path, len(time_list)))

    # 将时间戳转化成时间
    # for i in time_list:
    #     time_local = time.localtime(i)
    #     dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
    #     print(dt)

    # for i in range(10):
    #     tmp_file = open('tmp.yaml', "w")
    #     tmp_file.write(time_data[time_list[i]])
    #     tmp_file.close()

    return start_time, time_data


def export_image(output_path):
    # 循环读取bag
    count = 0

    for bag in bag_path:
        try:
            start_time, time_data = read_bag(bag, topic_list)
            for item in time_data.keys():
                time_local = time.localtime(item)
                dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
                export_path = str(dt)

                if not os.path.exists(output_path):
                    os.makedirs(output_path)

                # 修改yaml，过滤指定的topic
                camera_tmp_file = open(
                    "/home/holo/workspace/hpp_20201104/target/config/holo_data_provider/app_config/camera_tmp.yaml",
                    "w")
                camera_tmp_file.write(time_data[item])
                camera_tmp_file.close()

                print(export_path, time_data[item])

                os.system('/home/holo/workspace/hpp_20201104/target/bin/ros/export_3d_data_cmw '
                          '-i %s --camera_yaml_path '
                          '/home/holo/workspace/hpp_20201104/target/config/holo_data_provider/app_config/camera_tmp.yaml '
                          '--start %d --range %d -o %s '
                          '--output_camera_image 1' % (bag, item - start_time, 1, output_path + '/' + export_path))
        except Exception as e:
            print("ERROR: %s" % e)
            continue

        os.system('rm -f %s' % bag)
        count = count + 1
        print('\n\n====================================================================\n\n')
        print('process: %.3f' % (float(count) / len(bag_path)))
        print('\n\n====================================================================\n\n')


if __name__ == '__main__':
    topic_list = ['/holo/perception/vision/parking_freespace', '/holo/gateway/vehicle_info_weltmeister']
    # bag_path = '/home/holo/wzm_test/data/2020-11-10-16-40-37_fs.bag'
    # bag_path = ['/home/holo/bags/20201113/2020-11-13-11-23-45_route_31.bag']
    bag_path = []
    # bag_path = ['/home/holo/perception_data_filter/data/test_data/2020-12-02-17-00-43_hpp_50.bag']
    local_path = '/home/holo/perception_data_filter/data/20201030_oulu'
    # local_path = '/home/holo/bags/toyota_new'
    output_path = '/home/holo/perception_data_filter/output_data/picture'

    for root, dirs, files in os.walk(local_path):
        for file in files:
            if os.path.splitext(file)[1] == '.bag':
                bag_path.append(os.path.join(root, file))
    export_image(output_path)

    # read_bag(bag_path[0], topic_list)