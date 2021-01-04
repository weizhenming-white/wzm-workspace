#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-11-11 19:24
brief:分析freespace数据，增加freespace过滤逻辑 link analysis_fs_badcase.py
"""

import rosbag
import sys
import os
import math
import time

point_dict = {1: '/holo/sensors/camera/front_center_gs_h264',
              2: '/holo/sensors/camera/rear_center_h264',
              3: '/holo/sensors/camera/front_left_h264',
              4: '/holo/sensors/camera/front_right_h264'}


def read_bag(bag_path, topic_list):
    # 设置变量
    bag = rosbag.Bag(bag_path)
    time_list = []
    time_data = {}

    # tmp_txt = open('output/tmp.txt', 'w')
    for topic, msg, timestamp in bag.read_messages(topics=topic_list):

        tag_list = []
        if topic == '/holo/perception/vision/parking_freespace':
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

                # 基于车身前后3m, 左右2m范围进行过滤，如存在，则将tag置为1
                if (-3.934 <= x <= 6.65) and (-3 <= y <= 3):

                    # 判断当前点是否在第一象限，如在，则添加标志位1,3
                    if (x >= 0) and (y >= 0):
                        if 1 not in tag_list:
                            tag_list.append(1)
                        if 3 not in tag_list:
                            tag_list.append(3)

                    # 判断当前点是否在第二象限，如在，则添加标志位1,4
                    if (x >= 0) and (y <= 0):
                        if 1 not in tag_list:
                            tag_list.append(1)
                        if 4 not in tag_list:
                            tag_list.append(4)

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
                elif int(msg.obstacles[i].classification) == 1:
                    count = count + 1

            # 将出现空洞那一帧的时间戳添加到list里面
            # if count > 0:
            print('\n==============================\n')
            print(tag_list)
            secs = float(msg.header.stamp.secs)
            nsec = float(msg.header.stamp.nsecs) / 1000000000
            stamp = secs + nsec
            topic_filter = ''
            if len(tag_list) > 0:

                if len(time_list) == 0:
                    print('Add timestamp to list')

                    # 得到需要导出的图片的topic
                    for i in range(len(tag_list)):
                        if i == 0:
                            topic_filter = topic_filter + "topic == '%s'" % point_dict[tag_list[i]]
                        else:
                            topic_filter = topic_filter + " or topic == '%s'" % point_dict[tag_list[i]]
                    time_list.append(secs)
                    time_data[secs] = topic_filter
                else:
                    if secs != time_list[-1]:
                        topic_filter = ''
                        for i in range(len(tag_list)):
                            if i == 0:
                                topic_filter = topic_filter + "topic == '%s'" % point_dict[tag_list[i]]
                            else:
                                topic_filter = topic_filter + " or topic == '%s'" % point_dict[tag_list[i]]
                        time_list.append(secs)
                        time_data[secs] = topic_filter

            # print('no-freespace number is: ', count)

            # tmp_txt.write('\n==============================\n'
            #               + 'no-freespace number is: %d\n' % count
            #               + "This frame list count is %d\n" % len(msg.obstacles))

    # tmp_txt.write('\n\n' + str(time_list))
    # tmp_txt.close()
    # print(time_list)
    bag.close()
    print("%s has %d bad case." % (bag_path, len(time_list)))
    print(time_list)
    print(time_data)

    # 将时间戳转化成时间
    # for i in time_list:
    #     time_local = time.localtime(i)
    #     dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)
    #     print(dt)

    return time_data


def export_image():
    # 循环读取bag
    count = 0
    for bag in bag_path:
        time_data = read_bag(bag, topic_list)
        for item in time_data.keys():
            time_local = time.localtime(item)
            dt = time.strftime("%Y-%m-%d-%H-%M-%S", time_local)

            bag_tmp = os.path.join(os.getcwd(), str(dt) + '.bag')
            os.system('rosbag filter %s %s "(%s) and (t.to_sec() >= %.1f and t.to_sec() <= %.1f)"' % (bag, str(bag_tmp), time_data[item], item, item + 1))

            file_name = os.path.split(bag_tmp)[1]
            export_path = os.path.splitext(file_name)[0]
            if not os.path.exists('picture'):
                os.makedirs('picture')
            print(bag_tmp, export_path)
            os.system('/home/holo/workspace/hpp_20201104/target/bin/ros/export_3d_data_cmw '
                      '-i %s --camera_yaml_path '
                      '/home/holo/workspace/hpp_20201104/target/config/holo_data_provider/app_config/camera.yaml '
                      '-o %s --output_camera_image 1' % (bag_tmp, 'picture' + '/' + export_path))
            os.system('rm -f %s' % bag_tmp)
        os.system('rm -f %s' % bag)
        count = count + 1
        print('\n\n====================================================================\n\n')
        print('process: %.3f' % (count / len(bag_path)))
        print('\n\n====================================================================\n\n')


if __name__ == '__main__':
    topic_list = ['/holo/perception/vision/parking_freespace', '/holo/gateway/vehicle_info_weltmeister']
    # bag_path = '/home/holo/wzm_test/data/2020-11-10-16-40-37_fs.bag'
    # bag_path = ['/home/holo/bags/20201113/2020-11-13-11-23-45_route_31.bag']
    # bag_path = ['/home/holo/wzm_test/data/2020-11-09-13-37-15_route_1.bag']
    bag_path = []
    # local_path = '/home/holo/perception_data_filter/data'
    local_path = '/home/holo/bags/toyota_new'
    for root, dirs, files in os.walk(local_path):
        for file in files:
            if os.path.splitext(file)[1] == '.bag':
                bag_path.append(os.path.join(root, file))
    export_image()

    # export_image()
    # read_bag(bag_path[0], topic_list)