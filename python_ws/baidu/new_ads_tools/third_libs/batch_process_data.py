#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os


def read_txt(casename):
    """
    :from txt read src data
    :param filename:
    :return: data(dict)
    """

    path = ".\\raw_data\\"

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

    # 循环获取多组数据，并保存为列表格式
    all_data = list()
    for one in temp_list:
        valid_data = list()
        for i in path_and_filename:
            if one.split("-")[-2] in i:
                valid_data.append(i)

        data = dict()
        for iii in valid_data:
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
                        if "perception3d" in iii:
                            for i in range(len(row.split())):
                                line_data.append("perception3d_" + row.split()[i])
                        if "trafficlight" in iii:
                            for i in range(len(row.split())):
                                line_data.append("trafficlight_" + row.split()[i])
                    if m == 1:
                        for j in line_data:
                            data[j] = list()
                    if m != 1:
                        for mm in range(len(row.split())):
                            data[line_data[mm]].append(float(row.split()[mm]))
                    m += 1
        all_data.append(data)

    return all_data


if __name__ == '__main__':
    read_txt("B_acc_aeb_10")