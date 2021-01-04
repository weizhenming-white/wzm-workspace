#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
sys.path.append('/home/holo/perception_data_filter')

import rosbag
import os
import third_libs.data_filter as data_filter


def get_TimestampLinkSpeed(path, params):
    """
    #得到时间戳和车速对应的数据
    :param path:
    :param params:
    :return:
    """
    data = data_filter.bianli(path, params)
    for item in data:
        bag = rosbag.Bag(item)
        data = {}

        # 以bag作为文件名
        file_name = os.path.splitext(os.path.basename(item))[0]

        with open('../config/%s.txt' % file_name, 'w') as f:
            # for topic, msg, timestamp in bag.read_messages(topics='/holo/gateway/vehicle_info_jizhi'):
            for topic, msg, timestamp in bag.read_messages(topics='/holo/gateway/vehicle_info_weltmeister'):
                # print(msg)
                secs = float(msg.header.stamp.secs)
                nsec = float(msg.header.stamp.nsecs) / 1000000000
                stamp = round(secs + nsec, 3)
                speed = float(msg.vehicle_speed)
                f.write(str(stamp) + '\t' + str(speed) + '\n')
                print(stamp, speed)
                data[stamp] = speed

        bag.close()


def get_FreespaceLinkH264(path, params):
    """
    #得到时间戳和车速对应的数据
    :param path:需要筛选的路径
    :param params:需要过滤文件的后缀名
    :return:返回基于原始文件名进行命名的txt文件
    """
    data = data_filter.bianli(path, params)
    topic_list = ['/holo/gateway/vehicle_info_weltmeister',
                  '/holo/perception/vision/parking_freespace',
                  '/holo/sensors/camera/front_center_h264']

    for item in data:
        bag = rosbag.Bag(item)
        data = {}

        # 以bag作为文件名
        file_name = os.path.splitext(os.path.basename(item))[0]

        with open('../config/%s.txt' % file_name, 'w') as f:
            # for topic, msg, timestamp in bag.read_messages(topics='/holo/gateway/vehicle_info_jizhi'):
            for topic, msg, timestamp in bag.read_messages(topics='/holo/gateway/vehicle_info_weltmeister'):
                # print(msg)
                secs = float(msg.header.stamp.secs)
                nsec = float(msg.header.stamp.nsecs) / 1000000000
                stamp = round(secs + nsec, 3)
                speed = float(msg.vehicle_speed)
                f.write(str(stamp) + '\t' + str(speed) + '\n')
                print(stamp, speed)
                data[stamp] = speed

        bag.close()


def get_InitScreenData(path):
    data_timestamp = data_filter.bianli(path, '.txt')

    for item in data_timestamp:
        print(item)
        data_speed = {}
        output_data = []
        # 打开时间戳和速度对应文件
        print(item.split('/')[-5])
        with open('../config/%s.txt' % item.split('/')[-5]) as f:
            for line in f:
                data_speed[float(line.split()[0])] = float(line.split()[1])
        # print(data_speed)

        # 打开图片时间戳文件
        with open(item) as f:
            for line in f:
                tmp_stamp = float('%.2f' % float(line.split()[1]))
                try:
                    if data_speed[tmp_stamp] > 0:
                        print("timestamp is :", tmp_stamp, float(line.split()[0]))
                        output_data.append(float(line.split()[0]))
                except Exception as e:
                    print("The first error is ", e)
                    tmp_stamp = float('%.1f' % float(line.split()[1]))
                    try:
                        if data_speed[tmp_stamp] > 0:
                            print("The second success is ", tmp_stamp, data_speed[tmp_stamp], float(line.split()[0]))
                            output_data.append(float(line.split()[0]))
                    except Exception as e:
                        print("The second error is ", e, float(line.split()[0]))
                        output_data.append(float(line.split()[0]), )
        print(output_data)

        # 创建导出目录
        output_path = os.path.split(item)[0].split('raw_data')[0] + 'init_screen_data' + os.path.split(item)[0].split('raw_data')[1]
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        count = 0
        for i in output_data:
            old_name = os.path.join(os.path.split(item)[0], str(int(i)).zfill(8) + '.jpeg')
            new_name = os.path.join(output_path, str(count).zfill(8) + '.jpeg')
            print(old_name, new_name)
            os.system('cp %s %s' % (old_name, new_name))
            count += 1


def get_birdview():
    os.system()


if __name__ == '__main__':
    # get_TimestampLinkSpeed('/media/holo/data1/workspace_test/bags/20201210_aolai', '.bag')
    # get_TimestampLinkSpeed('/media/holo/data1/workspace_test/bags/20201215_aolai', '.bag')
    # get_TimestampLinkSpeed('/media/holo/data1/workspace_test/bags/20201221_aolai', '.bag')
    get_TimestampLinkSpeed('/media/holo/data1/workspace_test/bags/jizhi', '.bag')

    # get_InitScreenData('/media/holo/data1/workspace_test/perception_data/raw_data/20201210_aolai')
    # get_InitScreenData('/media/holo/data1/workspace_test/perception_data/raw_data/20201215_aolai')
    # get_InitScreenData('/media/holo/data1/workspace_test/perception_data/raw_data/20201221_aolai')
    # get_InitScreenData('/media/holo/data1/workspace_test/perception_data/raw_data/20201030_oulu')

    # path = '/media/holo/data1/workspace_test/perception_data/raw_data/20201219_aolai/2020-12-19-16-25-04_aolai/camera/front_left_h264/CAMERA_FRONT_LEFT/timestamps.txt'
    # print os.path.split(path)
    # print os.path.join(os.path.split(path)[0], str(0).zfill(8) + '.jpeg')