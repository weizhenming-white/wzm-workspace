#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:wzm
brief:画出control_command和vehicle_info里面的acc比较
"""
import rosbag
import matplotlib.pyplot as plt
import time

start_time = time.time()

#选择处理bag
bag = rosbag.Bag('/home/holo/bags/20200520/2020-05-20-11-28-37_hpp_2.bag')
# file_name = open("test.txt", "w")

#加载目标topic和字段，添加到列表
control_acc = list()
vehicle_acc = list()
vehicle_speed = list()
timestamp = list()
for topic, msg, t in bag.read_messages():
    if topic == "/holo/control/control_command":
        time_stamp = msg.header.stamp.secs
        acc = msg.acceleration
        control_acc.append(float(acc))
        timestamp.append(int(time_stamp))
    if topic == "/holo/gateway/vehicle_info_greatwall":
        acc = msg.longitude_acc
        speed = msg.vehicle_speed
        vehicle_acc.append(float(acc))
        vehicle_speed.append(float(speed))
    # file_name.write(str(msg) + "\n")
    # print(msg)
print "timestamp length is ", len(timestamp)
timestamp = list(set(timestamp))
print "timestamp length is ", len(timestamp)
# 画图
plt.figure("trajectory graph")
plt.plot(control_acc, "b", label="control_acc")
plt.plot(vehicle_acc, "r", label="vehicle_acc")
plt.plot(vehicle_speed, "y", label="vehicle_speed")
# plt.xticks(range(1, len(timestamp), 1))
plt.grid()                             # 面板网格化
plt.legend()                  # 显示图例
# plt.show()
plt.savefig("/home/holo/2020-05-20-11-28-37_hpp_2.png")

#关闭bag
bag.close()

time = time.time() - start_time
print "Execution Time is ", time
# file_name.close()