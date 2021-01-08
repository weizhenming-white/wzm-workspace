#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:魏振明
time:2020-12-08 15:44
brief:1. 遍历目录下的文件，找出后缀名为“jpeg”的文件，并修改文件名，移动到指定目录
      2. 批量修改文件名
"""
import os


def filter_1(path):
    """
    将图片规整到一个目录里面,并按照时间顺序修改文件名
    """
    count = 0
    # 在当前目录下创建文件夹‘all_image’
    output_path = '/home/holo/perception_data_filter/output_data/20201223_oulu'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # 过滤出后缀名为'.jpeg'的文件
            if os.path.splitext(file)[1] == '.jpeg':
                new_name_tmp = file_path.split('/')[-4] + '_' + file_path.split('/')[-2] + '_' + os.path.basename(file_path)
                # new_name_tmp = '20201202' + '_' + file_path.split('/')[-2] + '_' + os.path.basename(
                    # file_path)
                print(new_name_tmp)
                new_name = os.path.join(output_path, new_name_tmp)
                # print(file_path, os.path.basename(file_path), file_path.split('/')[-4], file_path.split('/')[-3])
                os.system('mv %s %s' % (file_path, output_path))
                # print(os.path.join(output_path, os.path.basename(file_path)))
                old_name = os.path.join(output_path, os.path.basename(file_path))
                os.renames(old_name, new_name)
                count += 1

        for dir in dirs:
            filter_1(dir)

    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print("=============================================================================================")


def filter_2(path, distance):
    """
    对数据进行采样，间隔step张图片抽一张
    """
    # 设置参数
    count = 0
    total = 0
    picture_path = []

    # 创建output path
    # output_path = path.split('raw_data')[0] + 'filter_data' + path.split('raw_data')[1]
    # print(path, output_path)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # 过滤出后缀名为'.jpeg'的文件
            if os.path.splitext(file)[1] == '.jpeg':

                count += 1
                print(file_path)
                print(os.path.splitext(file))

                if root not in picture_path:
                    picture_path.append(root)

        for dir in dirs:
            filter_2(dir, distance)
    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print("=============================================================================================")

    count_2 = 0
    print('\n\n\n\n\n\n')
    print(picture_path)

    for i in picture_path:

        # 得到该目录下的图片数量
        tmp = int(os.popen('ls %s | grep jpeg | wc -l' % i).read())
        print(tmp)

        # 创建筛选之后的目录
        output_path = i.split('init_screen_data')[0] + 'sampling_data' + i.split('init_screen_data')[1]
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 隔5s抽一张(25张抽一张)
        step = 0
        for item in range(tmp):
            if (item == step) and step < tmp:
                old_name = os.path.join(i, str(item).zfill(8) + '.jpeg')
                new_name = old_name.split('init_screen_data')[0] + 'sampling_data' + old_name.split('init_screen_data')[1]
                print(old_name, new_name)
                os.system('cp %s %s' % (old_name, new_name))
                step += distance


def filter_3(path):
    """
    统计目录下的图片数量
    """
    # 设置参数
    count = 0
    front_wide_count = 0
    front_sv_count = 0
    left_sv_count = 0
    right_sv_count = 0
    rear_sv_count = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # 过滤出后缀名为'.jpeg'的文件，并统计
            if os.path.splitext(file)[1] == '.jpeg':
                print(file_path)
                count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_CENTER':
                    front_wide_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_CENTER_GS':
                    front_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_LEFT':
                    left_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_FRONT_RIGHT':
                    right_sv_count += 1
                if file_path.split('/')[-2] == 'CAMERA_REAR_CENTER':
                    rear_sv_count += 1

        for dir in dirs:
            filter_3(dir)
    print("\n\n=============================================================================================")
    print('The total is %d' % count)
    print('The front wide number is %d' %front_wide_count)
    print('The front sv number is %d' % front_sv_count)
    print('The left sv number is %d' % left_sv_count)
    print('The right sv number is %d' % right_sv_count)
    print('The rear sv number is %d' % rear_sv_count)
    print("=============================================================================================")


def filter_4(path, output_path):
    """
    修改文件，更新文件存放方式。例：
    原文件：2020-12-19-16-51-19_CAMERA_FRONT_CENTER_GS_00000003.jpeg
    修改后：camera/front_center_gs_h264/CAMERA_FRONT_CENTER_GS/00000003.jpeg
    """
    # 设置变量
    front_wide = 0
    front_sv = 0
    rear_sv = 0
    left_sv = 0
    right_sv = 0

    path_tmp = os.path.join(output_path, 'camera')
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if 'CAMERA_FRONT_CENTER_0' in file:
                export_front_wide = os.path.join(path_tmp, 'front_center_h264/' + 'CAMERA_FRONT_CENTER/')
                if not os.path.exists(export_front_wide):
                    os.makedirs(export_front_wide)
                print(file_path, os.path.join(export_front_wide, str(front_wide).zfill(8) + '.jpeg'))
                os.system('cp %s %s' % (file_path, os.path.join(export_front_wide, str(front_wide).zfill(8) + '.jpeg')))
                front_wide += 1
            if 'CAMERA_FRONT_CENTER_GS_0' in file:
                export_front_sv = os.path.join(path_tmp, 'front_center_gs_h264/' + 'CAMERA_FRONT_CENTER_GS/')
                if not os.path.exists(export_front_sv):
                    os.makedirs(export_front_sv)
                print(file_path, os.path.join(export_front_sv, str(front_sv).zfill(8) + '.jpeg'))
                os.system('cp %s %s' % (file_path, os.path.join(export_front_sv, str(front_sv).zfill(8) + '.jpeg')))
                front_sv += 1
            if 'CAMERA_FRONT_LEFT_0' in file:
                export_left_sv = os.path.join(path_tmp, 'front_left_h264/' + 'CAMERA_FRONT_LEFT/')
                if not os.path.exists(export_left_sv):
                    os.makedirs(export_left_sv)
                print(file_path, os.path.join(export_left_sv, str(left_sv).zfill(8) + '.jpeg'))
                os.system('cp %s %s' % (file_path, os.path.join(export_left_sv, str(left_sv).zfill(8) + '.jpeg')))
                left_sv += 1
            if 'CAMERA_FRONT_RIGHT_0' in file:
                export_right_sv = os.path.join(path_tmp, 'front_right_h264/' + 'CAMERA_FRONT_RIGHT/')
                if not os.path.exists(export_right_sv):
                    os.makedirs(export_right_sv)
                print(file_path, os.path.join(export_right_sv, str(right_sv).zfill(8) + '.jpeg'))
                os.system('cp %s %s' % (file_path, os.path.join(export_right_sv, str(right_sv).zfill(8) + '.jpeg')))
                right_sv += 1
            if 'CAMERA_REAR_CENTER_0' in file:
                export_rear_sv = os.path.join(path_tmp, 'rear_center_h264/' + 'CAMERA_REAR_CENTER/')
                if not os.path.exists(export_rear_sv):
                    os.makedirs(export_rear_sv)
                print(file_path, os.path.join(export_rear_sv, str(rear_sv).zfill(8) + '.jpeg'))
                os.system('cp %s %s' % (file_path, os.path.join(export_rear_sv, str(rear_sv).zfill(8) + '.jpeg')))
                rear_sv += 1


import rosbag


def filter_5(bag_path, topic_list):
    """
    过滤出时间戳对应的速度，并保存为文件
    """
    # 设置变量
    for bag_name in bag_path:
        bag = rosbag.Bag(bag_name)
        data = {}

        # 以bag作为文件名
        file_name = os.path.splitext(os.path.basename(bag_path))[0]

        with open('../config/%s.txt' % file_name, 'w') as f:
            for topic, msg, timestamp in bag.read_messages(topics=topic_list):
                # print(msg)
                secs = float(msg.header.stamp.secs)
                nsec = float(msg.header.stamp.nsecs) / 1000000000
                stamp = round(secs + nsec, 3)
                speed = float(msg.vehicle_speed)
                f.write(str(stamp) + '\t' + str(speed) + '\n')
                print(stamp, speed)
                data[stamp] = speed

        bag.close()


def filter_6(raw_data):
    """
    删除静止数据
    """
    # 设置文件名和存放变量
    timestamps_txt = os.path.join(raw_data, 'timestamps.txt')
    data = {}
    output_data = []

    # 打开时间戳和速度对应文件
    with open('../config/2020-12-19-13-55-04_aolai.txt') as f:
        for line in f:
            data[float(line.split()[0])] = float(line.split()[1])

    # 打开图片时间戳文件
    with open(timestamps_txt) as f:
        for line in f:
            tmp_stamp = float('%.2f' % float(line.split()[1]))
            try:
                if data[tmp_stamp] > 0:
                    print(tmp_stamp)
                    output_data.append(float(line.split()[0]))
            except Exception as e:
                print e
                tmp_stamp = float('%.1f' % float(line.split()[1]))
                try:
                    if data[tmp_stamp] > 0:
                        print("error", tmp_stamp, data[tmp_stamp])
                        output_data.append(float(line.split()[0]))
                except Exception as e:
                    print e
                    output_data.append(float(line.split()[0]))
    print(output_data)




def rename_file(path, output_path):
    """
    批量修改文件名，按照指定序号
    camera/front_center_gs_h264/CAMERA_FRONT_CENTER_GS/00000003.jpeg
    """
    front_wide = 0
    front_sv = 0
    rear_sv = 0
    left_sv = 0
    right_sv = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_CENTER':
                export_front_wide = os.path.join(output_path, 'CAMERA_FRONT_CENTER/')
                if not os.path.exists(export_front_wide):
                    os.makedirs(export_front_wide)
                os.system('cp %s %s' % (file_path, os.path.join(export_front_wide, str(front_wide).zfill(8) + '.jpeg')))
                front_wide += 1
                print('rename front wide')
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_CENTER_GS':
                export_front_sv = os.path.join(output_path, 'CAMERA_FRONT_CENTER_GS/')
                if not os.path.exists(export_front_sv):
                    os.makedirs(export_front_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_front_sv, str(front_sv).zfill(8) + '.jpeg')))
                front_sv += 1
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_LEFT':
                export_left_sv = os.path.join(output_path, 'CAMERA_FRONT_LEFT/')
                if not os.path.exists(export_left_sv):
                    os.makedirs(export_left_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_left_sv, str(left_sv).zfill(8) + '.jpeg')))
                left_sv += 1
            if str(file_path.split('/')[-2]) == 'CAMERA_FRONT_RIGHT':
                export_right_sv = os.path.join(output_path, 'CAMERA_FRONT_RIGHT/')
                if not os.path.exists(export_right_sv):
                    os.makedirs(export_right_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_right_sv, str(right_sv).zfill(8) + '.jpeg')))
                right_sv += 1
            if str(file_path.split('/')[-2]) == 'CAMERA_REAR_CENTER':
                export_rear_sv = os.path.join(output_path, 'CAMERA_REAR_CENTER/')
                if not os.path.exists(export_rear_sv):
                    os.makedirs(export_rear_sv)
                os.system('cp %s %s' % (file_path, os.path.join(export_rear_sv, str(rear_sv).zfill(8) + '.jpeg')))
                rear_sv += 1



if __name__ == '__main__':
    # bianli('/home/holo/perception_data_filter/output_data/picture')
    # rename_file('/home/holo/perception_data_filter/tmp')

    # filter_1('/home/holo/perception_data_filter/output_data/picture')
    # filter_1('/home/holo/perception_data_filter/output_data/picture')

    # filter_2('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201219_aolai', 10)
    # filter_2('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201210_aolai', 10)
    # filter_2('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201215_aolai', 10)
    # filter_2('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201221_aolai', 10)
    # filter_2('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201030_oulu', 10)
    # filter_2('/media/holo/data/workspace_test/perception_data/init_screen_data/jizhi', 10)

    # filter_3('/media/holo/data1/workspace_test/perception_data/raw_data/20201219_aolai')    # 158106
    # filter_3('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201219_aolai')  # 129974
    # filter_3('/media/holo/data1/workspace_test/perception_data/detection/20201219_aolai')    # 13018
    # filter_3('/media/holo/data1/workspace_test/perception_data/raw_data/20201210_aolai')    # 37227
    # filter_3('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201210_aolai')    # 25900
    # filter_3('/media/holo/data1/workspace_test/perception_data/detection/20201210_aolai')   # 2623
    # filter_3('/media/holo/data1/workspace_test/perception_data/raw_data/20201215_aolai')    # 46589
    # filter_3('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201215_aolai')    # 37861
    # filter_3('/media/holo/data1/workspace_test/perception_data/detection/20201215_aolai')   # 3812
    # filter_3('/media/holo/data1/workspace_test/perception_data/raw_data/20201221_aolai')    # 180693
    # filter_3('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201221_aolai')  # 172919
    # filter_3('/media/holo/data1/workspace_test/perception_data/detection/20201221_aolai')   # 17296
    # filter_3('/media/holo/data1/workspace_test/perception_data/raw_data/20201222_aolai')    # 97129
    # filter_3('/media/holo/data1/workspace_test/perception_data/init_screen_data/20201222_aolai')  # 95653
    # filter_3('/media/holo/data1/workspace_test/perception_data/detection/20201222_aolai')   # 9567
    filter_3('/media/holo/data/workspace_test/perception_data/finally_data/Output_jizhi')

    # filter_4('/media/holo/data1/workspace_test/perception_data/filter_data/maquanyingaolai_20201215',
    #          '/media/holo/data1/workspace_test/perception_data/filter_data/maquanyingaolai_20201215/image_data')
    # filter_4('/home/holo/perception_data_filter/output_data/20201030_oulu',
    #          '/media/holo/data1/workspace_test/perception_data/filter_data/20201030_oulu/image_data')
    # filter_5('/media/holo/data1/workspace_test/bags/20201219_aolai/2020-12-19-13-55-04_aolai.bag', '/holo/gateway/vehicle_info_weltmeister')
    # filter_6('/media/holo/data1/workspace_test/perception_data/raw_data/20201219_aolai/2020-12-19-13-55-04_aolai/camera/front_center_gs_h264/CAMERA_FRONT_CENTER_GS')
    # rename_file('/media/holo/data/workspace_test/perception_data/sampling_data/jizhi', '/media/holo/data/workspace_test/perception_data/finally_data/jizhi')