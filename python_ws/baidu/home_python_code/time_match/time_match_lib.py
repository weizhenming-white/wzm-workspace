#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import commonlib.handletxtlib as handletxtlib


def get_data():
    m = 1
    data = {}
    line_data = []
    with open(r".\data\thwautostatus-turn-head-20km-3.txt") as f:
        for row in f:
            if m == 1:
                for i in range(len(row.split())):
                    line_data.append(row.split()[i])
            if m == 1:
                for j in line_data:
                    data[j] = list()
            if m != 1:
                for m in range(len(row.split())):
                    data[line_data[m]].append(row.split()[m])
            m += 1
    print data.keys()
    return data


def read_74log():

    value = {"timestamp": list(),
             "position_x": list(),
             "position_y": list(),
             "speed_x": list(),
             "speed_y": list(),
             "a_x": list(),
             "a_y": list()}

    filename = "dudrive_gateway.log.20180803-110701.2782.json"
    with open(r"data\%s" % filename) as f:
        data = json.loads(f.read())
        for num in range(len(data)):
            value["timestamp"].append(float(data[str(num)]["timestamp"]))
            value["position_x"].append(float(str(data[str(num)]["position"]).split(" ")[2]))
            value["position_y"].append(float(str(data[str(num)]["position"]).split(" ")[4]))
            value["speed_x"].append(float(str(data[str(num)]["linear_velocity"]).split(" ")[2]))
            value["speed_y"].append(float(str(data[str(num)]["linear_velocity"]).split(" ")[4]))
            value["a_x"].append(float(str(data[str(num)]["linear_acceleration"]).split(" ")[2]))
            value["a_y"].append(float(str(data[str(num)]["linear_acceleration"]).split(" ")[4]))
    return value


def analysis():
    auto_data = get_data()
    mkz74_data = read_74log()

    result_data = []
    for i in range(len(auto_data["timestamp"])):
        middle_list = list()
        timestamp_list = list()
        middle_data = list()
        for j in range(len(mkz74_data["timestamp"])):
            if float(auto_data["timestamp"][i]) + 0.5 >= \
                    mkz74_data["timestamp"][j] >= \
                    float(auto_data["timestamp"][i]) - 0.5:
                middle_list.append(mkz74_data[j][0])
                timestamp_list.append(mkz74_data[j][0])
                middle_data.append(mkz74_data[j])
        middle_list.append(float(auto_data["timestamp"][i]))
        middle_list.sort()


if __name__ == '__main__':
    analysis()




