#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
:author:
    wangxiaolong(wangxiaolong03@baidu.com)
:create_date:
    2018.07.24 15:10:52
:descrition:
    common
"""

import os
import sys
import logging
import logging.handlers


def print_log(filename, format=None):
    """
    :param filename:
    :param format:
    :return:
    """
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)
    rHandler = logging.handlers.RotatingFileHandler(filename + ".log",
                                                    maxBytes=10 * 1024 * 1024,
                                                    backupCount=3)
    rHandler.setLevel(logging.INFO)

    if format is None:
        formatter = logging.Formatter('[%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(lineno)d] '
                               '- %(message)s')
    else:
        formatter = format

    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger


def get_process_data(path, filename, offset, label, save_name=None):
    """
    get process data
    """
    data = handletxtlib.read_txt(path, filename)
    print data.keys()

    value = dict()
    for i in range(0, len(label)):
        value[label[i]] = list()
    for i in range(0, len(data["timestamp"])):
        if data["status"][i] == '1' or data["status"][i] == 1:
            for key in label:
                value[key].append(float(data[key][i]))
    print "get src data"

    temp = data_compensation(value, offset)

    if temp is None:
        print "data_compensation is None"
        return None

    value = temp
    if save_name is not None:
        if 1 == handletxtlib.save_data_to_txt(path, "compensation-" + filename, value):
            print "fail save compensation data"
        else:
            print "save compensation data success"

    return value


def data_compensation(data, offset):
    """
    compensation data
    :param data:
    :param offset:
    :return:
    """
    try:
        for i in range(0, len(data["timestamp"])):
            data["thw"][i] = (data["distance"][i] - offset) / data["auto-speed"][i]
            try:
                data["ttc"][i] = (data["distance"][i] - offset) / data["respeed"][i]
            except Exception as e:
                pass

        for i in range(0, len(data["timestamp"])):
            if "distance" in data.keys():
                data["distance"][i] = data["distance"][i] - offset
            if "auto-speed" in data.keys():
                data["auto-speed"][i] = data["auto-speed"][i] * 3.6
            try:
                if "respeed" in data.keys():
                    data["respeed"][i] = data["respeed"][i] * 3.6
            except Exception as e:
                pass

    except Exception as e:
        print "error data:", e
        return None

    return data


def get_times_data(data, start_time, end_time):
    """
    :get the data from start_time to end_time
    :param data:
    :param start_time:
    :param end_time:
    :return: value
    """
    value = dict()
    strkeys = data.keys()
    for key in strkeys:
        value[key] = list()
    try:
        for i in range(0, len(data["autoobs_timestamp"])):
            if data["autoobs_timestamp"][i] > start_time and data[
                "autoobs_timestamp"][i] < end_time:
                for key in strkeys:
                    value[key].append(float(data[key][i]))
    except Exception as e:
        print "Not get data", e
        return None

    return value

