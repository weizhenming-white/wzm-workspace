#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
:author:
    wangxiaolong(wangxiaolong03@baidu.com)
:create_date:
    2018.05.20 16:50:50
:descrition:
    get acc infor
"""

import os
import sys
import third_libs.alg_recognition_speed_down_lib as alg_recognition_speed_down_lib
import third_libs.data_filter as common
import third_libs.deal_rawdata_lib as deal_rawdata_lib


def acc_follow_obs(src_data, set_speed, offset):
    """
    acc follow obs
    """

    # 设置跟车速度，以及静态偏差、创建跟车数据存放处：data
    data = dict()

    for i in src_data.keys():
        if "autoobs_" in i:
            data[i] = list()

    # 过滤出自动驾驶的数据
    for i in range(len(src_data["autoobs_timestamp"])):
        if src_data["autoobs_status"][i] == float(1):
            for key in data.keys():
                data[key].append(src_data[key][i])

    # 计算出减去静态偏差后的ttc、thw
    for i in range(len(data["autoobs_timestamp"])):
        data["autoobs_thw"][i] = (data["autoobs_distance"][i] - offset
                                  ) / data["autoobs_auto-speed"][i]
        try:
            data["autoobs_ttc"][i] = (data["autoobs_distance"][i] - offset
                                      ) / data["autoobs_respeed"][i]
        except Exception as e:
            pass

    # 计算出减去静态偏差后的距离，并将速度转化成km/h
    for i in range(len(data["autoobs_timestamp"])):
        data["autoobs_distance"][i] = data["autoobs_distance"][i] - offset
        data["autoobs_auto-speed"][i] = data["autoobs_auto-speed"][i] * 3.6
        data["autoobs_respeed"][i] = data["autoobs_respeed"][i] * 3.6

    edge = alg_recognition_speed_down_lib.recognition_down_speed(data)

    count = len(edge["start"])
    if count == 0:
        if abs(data["autoobs_auto-speed"][0] - set_speed) <= set_speed * 0.20 and \
                        abs(data["autoobs_auto-speed"][-1] - set_speed) <= set_speed * 0.20:
            return data
        else:
            return None

    elif count == 1:
        if abs(data["autoobs_auto-speed"][0] - set_speed) <= set_speed * 0.20:
            return common.get_times_data(data, data["autoobs_timestamp"][0],
                                         edge["start"][0][0])
        else:
            return None

    else:
        end_time = 0
        for i in range(0, len(edge["start"])):
            if abs(data["autoobs_auto-speed"][edge["start"][count - 1 - i][1]] - set_speed) \
                    < set_speed * 0.20:
                end_time = edge["start"][count - 1 - i][0]
                break
    if end_time == 0 or edge["start"][0][0] == end_time:
        if abs(data["autoobs_auto-speed"][0] - set_speed) <= set_speed * 0.20:
            return common.get_times_data(data, data["autoobs_timestamp"][0],
                                         edge["start"][0][0])
        else:
            return None

    # 将原始数据重新加入到新的字典里
    new_data = common.get_times_data(data, edge["start"][0][0], end_time)

    for i in src_data.keys():
        if "autoobs_" not in i:
            new_data[i] = src_data[i]

    return new_data


if __name__ == "__main__":
    print "test"

