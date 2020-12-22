#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json


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
    filename = "dudrive_gateway.log.20180803-110701.2782.json"
    mkz74_data = []
    with open(r"data\%s" % filename) as f:
        data = json.loads(f.read())
        for num in range(len(data)):
            timestamp = float(data[str(num)]["timestamp"])
            linear_velocity = data[str(num)]["linear_velocity"]
            speed_x = str(data[str(num)]["linear_velocity"]).split(" ")[2]
            speed_y = str(data[str(num)]["linear_velocity"]).split(" ")[4]
            speed = pow((pow(float(speed_x), 2) + pow(float(speed_y), 2)), (1.0 / 2)) * 3.6
            position = str(data[str(num)]["position"])
            linear_acceleration = data[str(num)]["linear_acceleration"]
            a_y = str(linear_acceleration).split(" ")[4]
            mkz74_data.append([timestamp, speed, position, a_y])
    return mkz74_data


def get_position():
    mkz74_data = read_74log()
    point_x = 433310.067135
    point_y = 4437230.074946

    distan = list()
    for m in range(len(mkz74_data)):
        l = pow(pow((point_x - float(mkz74_data[m][2].split(" ")[2])), 2)
                + pow((point_y - float(mkz74_data[m][2].split(" ")[4])), 2), (1.0 / 2))
        distan.append(l)
    global key_x, key_y
    key_x = float(mkz74_data[distan.index(min(distan))][2].split(" ")[2])
    key_y = float(mkz74_data[distan.index(min(distan))][2].split(" ")[4])
    print "预测碰撞点坐标：", key_x, key_y


def analysis():
    auto_data = get_data()
    mkz74_data = read_74log()

    result_data = list()
    distan_list = list()
    for i in range(len(auto_data["timestamp"])):
        middle_list = list()
        timestamp_list = list()
        middle_data = list()
        for j in range(len(mkz74_data)):
            if float(auto_data["timestamp"][i]) + 0.5 >= mkz74_data[j][0] >= float(auto_data["timestamp"][i]) - 0.5:
                middle_list.append(mkz74_data[j][0])
                timestamp_list.append(mkz74_data[j][0])
                middle_data.append(mkz74_data[j])
        middle_list.append(float(auto_data["timestamp"][i]))
        middle_list.sort()

        speed = middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][1]
        x0 = key_x - float(middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][2].split(" ")[2])
        y0 = key_y - float(middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][2].split(" ")[4])
        distan = pow((pow(x0, 2) + pow(y0, 2)), (1.0 / 2))
        distan_list.append(distan)
        result_data.append([speed, distan])

        print "主车时间：", float(auto_data["timestamp"][i]), "\t", \
            "障碍车时间：", middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][0]
        print "主车位置：", auto_data["position_x"][i], auto_data["position_y"][i]
        print "障碍车位置：", middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][2].split(" ")[2], \
            middle_data[middle_list.index(float(auto_data["timestamp"][i])) - 1][2].split(" ")[4]
        print speed, distan

        print "数据长度：", len(middle_list)
    num = distan_list.index(min(distan_list))
    print distan_list
    file = open(r".\output\result-thwautostatus-turn-head-20km-3.txt", "w")
    msg = str()
    for ii in auto_data.keys():
        msg = msg + ii + "\t"
    file.write(msg + "obs-distan\t" + "obs-thw\t" + "obs-speed\t" + "ttc\n")
    file.close()

    for mm in range(len(result_data)):
        message = str()
        for nn in auto_data.keys():
            message = message + str(auto_data[nn][mm]) + "\t"
        if mm <= num:
            if distan_list[mm] >= 3.8:
                dis = distan_list[mm] - 3.8
                thw = (distan_list[mm] - 3.8) / result_data[mm][0]
                ttc = float(auto_data["thw"][mm]) - thw
            else:
                dis = float(0)
                thw = dis / result_data[mm][0]
                ttc = float(auto_data["thw"][mm]) - thw
        else:
            if distan_list[mm] >= 1.1:
                dis = (distan_list[mm] - 1.1) * -1
                thw = dis / result_data[mm][0]
                ttc = float(auto_data["thw"][mm]) - thw
            else:
                dis = float(0)
                thw = dis / result_data[mm][0]
                ttc = float(auto_data["thw"][mm]) - thw
        with open(r".\output\result-thwautostatus-turn-head-20km-3.txt", "a+") as f:
            f.write(message + str(dis) + "\t" + str(thw)
                    + "\t" + str(result_data[mm][0])
                    + "\t" + str(ttc) + "\n")


if __name__ == '__main__':
    get_position()
    analysis()




