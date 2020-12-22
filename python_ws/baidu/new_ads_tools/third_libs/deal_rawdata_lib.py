#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


def read_txt(casename):
    """
    读取一个场景最新的原始数据，并保存在字典里
    """

    path = r"/Users/baidu/Desktop/new_ads_tools/raw_data"

    # 遍历目录，找出对应case的文件
    filename_list = list()
    path_and_filename = list()
    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:
            if casename in i:
                filename_list.append(i)
                path_and_filename.append(os.path.join(dirpath, i))

    # 找出当前case最新的测试txt，以"autostatus"目录下的为判断依据
    temp_list = list()
    for i in filename_list:
        if "autostatus" in i:
            temp_list.append(i)

    # 对文件进行排序（冒泡法）
    for i in range(len(temp_list)):
        for j in range(i + 1, len(temp_list)):
            a = temp_list[i].split("-")[1].split("_")[-1]
            b = temp_list[j].split("-")[1].split("_")[-1]
            if int(a) > int(b):
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]

    # 将当前场景的最新测试txt加到一个列表里
    valid_filename_list = list()
    for i in path_and_filename:
        if temp_list[-1].split("-")[1] in i:
            valid_filename_list.append(i)

    # 保存的数据变量
    data = dict()

    # 将这些符合要求的数据保存到一个dict里面
    for iii in valid_filename_list:
        m = 1
        line_data = list()
        with open(iii) as f:
            for row in f:
                if m == 1:
                    if "autoobs" in iii:
                        for i in range(len(row.split())):
                            line_data.append("autoobs_" + row.split()[i])
                    if "autostatus" in iii:
                        for i in range(len(row.split())):
                            line_data.append("autostatus_" + row.split()[i])
                    if "trafficlight" in iii:
                        for i in range(len(row.split())):
                            line_data.append("trafficlight_" + row.split()[i])
                    if "perception3d" in iii:
                        for i in range(len(row.split())):
                            line_data.append("perception3d_" + row.split()[i])
                if m == 1:
                    for j in line_data:
                        data[j] = list()
                if m != 1:
                    for mm in range(len(row.split())):
                        data[line_data[mm]].append(float(row.split()[mm]))
                m += 1

    # 将障碍物的水平面积组成一个新的键值加到字典里。命名为：volume
    for i in data.keys():
        if "perception3d_v-x" or "perception3d_v-y" in i:
            data["volume"] = list()
            break

    for i, j in zip(data["perception3d_v-x"], data["perception3d_v-y"]):
        data["volume"].append(i * j)

    return data


def basic_index(field):
    """
    获取基础指标数据，例如：平均值、最大值、最小值、平均差，99分位等
    """

    _ave = sum(field) / len(field)
    _max = max(field)
    _min = min(field)

    # 平均差
    temp = list()
    for i in field:
        temp.append(pow((i - _ave), 2))
    _std = pow(sum(temp) / len(field), (1.0 / 2))

    # 99分位
    field.sort()
    _99fenwei = field[int(len(field) * 0.99)]

    # 保存为字典
    basic_data = dict()
    basic_data["ave"] = _ave
    basic_data["max"] = _max
    basic_data["min"] = _min
    basic_data["std"] = _std
    basic_data["99fenwei"] = _99fenwei

    return basic_data


if __name__ == '__main__':
    print os.getcwd()
    print read_txt("B_static_car").keys()