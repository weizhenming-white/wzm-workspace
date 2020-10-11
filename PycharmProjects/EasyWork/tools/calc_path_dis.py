#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:weizhenming@holomatic.com
time:2020-08-24 15:36
brief:计算地图路径长度
"""
import matplotlib.pyplot as plt


def CalcPathDistance(route_id):

    dis_list = list()
    heading_list = list()
    with open(file_name) as f:
        for i in f:
            x = i.split(":")[3].split(" ")[6]
            y = i.split(":")[3].split(" ")[7]
            z = i.split(":")[3].split(" ")[8]
            dis_list.append((float(x), float(y)))
            print x, y, z
            heading_list.append(float(z))

    dis = 0
    for i in range(0, len(dis_list)):
        if i == 0:
            continue
        tmp = pow(dis_list[i][0] - dis_list[i -1][0], 2) + pow(dis_list[i][1] - dis_list[i - 1][1], 2)
        dis = dis + pow(tmp, (1.0 / 2))

    # 绘制z值
    plt.figure("heading graph")
    plt.scatter(range(0, len(heading_list)), heading_list)
    plt.xlim(0, len(heading_list))
    plt.grid()
    # plt.xticks(range(0, len(heading_list), 10))

    #折线图
    # plt.plot(range(0, len(heading_list)), heading_list)
    # plt.grid()
    # plt.xlim(0, len(heading_list) -1)
    # plt.ylim(-1, 1)
    plt.savefig("output/test.png")

    return dis


if __name__ == '__main__':
    route_id = "route_3"
    file_name = r'/opt/holo/hpp/%s/vehicle_odometry.txt' % route_id
    dis = CalcPathDistance(file_name)
    print "The %s total length of the path is: %fm" % (route_id, dis)