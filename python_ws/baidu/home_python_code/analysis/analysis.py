#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
:author:
    wangxiaolong(wangxiaolong03@baidu.com)
:create_date:
    2018.04.19 12:58:50
:last_date:
    2018.04.19 14:28:00
:descrition:
"""
import re
import json
import ConfigParser


def open_file():
    """
    open dudrive_gateway.INFO
    """

    with open(r'D:\workspace\python_code\time_match\data\%s' % xxx) as f:
        data = f.read()
    return data


def get_timestamp():
    """
    get timestamp
    """
    data = open_file()
    re_filter01 = re.compile('timestamp_sec: (.*?) module_name: "gateway"')
    timestamp = re_filter01.findall(data)
    return timestamp


def get_position():
    """
    get position
    """
    data = open_file()
    re_filter02 = re.compile('position (.*?) orientation', re.S)
    position = re_filter02.findall(data)
    return position


def get_linear_velocity():
    """
    get linear_velocity
    """
    data = open_file()
    re_filter03 = re.compile('linear_velocity (.*?) linear_acceleration', re.S)
    linear_velocity = re_filter03.findall(data)
    return linear_velocity


def get_steering_percentage():
    """
    get steering_percentage
    """
    data = open_file()
    re_filter = re.compile('steering_percentage: (.*?) steering_torque_nm', re.S)
    steering_percentage = re_filter.findall(data)
    return steering_percentage


def get_linear_acceleration():
    """
    linear_acceleration
    """
    data = open_file()
    re_filter = re.compile('linear_acceleration (.*?) angular_velocity', re.S)
    linear_acceleration = re_filter.findall(data)
    return linear_acceleration


def save_data():
    """
    save analysis data
    """
    print "start deal with " + xxx
    timestamp = get_timestamp()
    position = get_position()
    linear_velocity = get_linear_velocity()
    steering_percentage = get_steering_percentage()
    linear_acceleration = get_linear_acceleration()

    data_dict = {}
    total = 0
    for i in range(0, len(timestamp)):
        try:
            data_dict[i] = {}
            data_dict[i]["timestamp"] = timestamp[i]
            data_dict[i]["position"] = position[i]
            data_dict[i]["linear_velocity"] = linear_velocity[i]
            data_dict[i]["steering_percentage"] = steering_percentage[i]
            data_dict[i]["linear_acceleration"] = linear_acceleration[i]
        except:
            total += 1
            continue
    print(total)

    data_json = json.dumps(data_dict)
    with open(r'D:\workspace\python_code\time_match\data\%s.json' % xxx, 'w') as f:
        f.write(data_json)


if __name__ == "__main__":
    global i
    file_list = ["dudrive_gateway.log.20180803-110701.2782"]
    for xxx in file_list:
        save_data()
    print "Success!!!"

