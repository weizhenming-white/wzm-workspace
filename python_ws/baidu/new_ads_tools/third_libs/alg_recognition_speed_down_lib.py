#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
:author:
    wangxiaolong(wangxiaolong03@baidu.com)
:create_date:
    2018.07.24 16:50:50
:descrition:
    recognition speed down
"""

import os
import math
import sys


def recognition_down_speed(value):
    """
    auto recongnition edge
    """
    STEP = 50
    car_slow = {
        "start": list(),
        "end": list(),
        "time_len": list()
    }
    if len(value["autoobs_timestamp"]) < 50:
        return None
    k = 50
    flag = 0
    while True:
        negative_a_count = 0
        for j in range(k - STEP, k):  # 阈值 100 ，可以修改
            if value["autoobs_auto-a-y"][j] < 0:
                negative_a_count = negative_a_count + 1
        per = 1.0 * negative_a_count / STEP
        if per > 0.90:
            if flag == 0:
                car_slow["start"].append([value["autoobs_timestamp"][k - STEP], k - STEP])
            k = k + STEP
            flag = flag + 1
        else:
            k = k + 1
            if flag > 0:
                car_slow["end"].append([value["autoobs_timestamp"][k - STEP], k - STEP])
            flag = 0
        #print "aaaaa", k, len(value["autoobs_timestamp"])
        if k >= len(value["autoobs_timestamp"]):
            break
    if len(car_slow["start"]) == len(car_slow["end"]):
        for i in range(0, len(car_slow["start"])):
            car_slow["time_len"].append(car_slow["end"][i][0] - car_slow["start"][i][0])
    else:
        for i in range(0, len(car_slow["end"])):
            car_slow["time_len"].append(car_slow["end"][i][0] - car_slow["start"][i][0])
        car_slow["time_len"].append(value["autoobs_timestamp"][
                                        len(value["autoobs_timestamp"]) - 1] - car_slow[
            "start"][len(car_slow["start"]) - 1][0])

        car_slow["end"].append([value["autoobs_timestamp"][len(value["autoobs_timestamp"]) - 1],
                                len(value["autoobs_timestamp"]) - 1])

    print len(value["autoobs_timestamp"]), len(car_slow["start"]), len(car_slow["end"])

    return car_slow