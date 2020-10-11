#!/usr/bin/python
# -*- coding=utf-8 -*-

'''
Ident.py - Python 3.6.8

Run as:
    python [-h] [-v] [--config_file] [path] [--show] [is_show]
    input arguments:
        path        parse all bag file under the path
        is_show     1 is show the fitting picture, 0 is not show

    optional arguments:
        -h          show this help message and exit
        -v          show the version of this program and exit

Example:
    python ident.py --config_file /home/holo/bag/ --show 0

Output as:
    ident.py:
    print fitting result in the terminal
'''

import os
import math
import matplotlib.pyplot as plt
import numpy as np
import rosbag
import sys, getopt
from scipy import optimize

topics_name = ["/holo/car_state_hpp",
               "/holo/sensors/novatel/odometry"
               ]
# ---------------------------------------
lfr = 2.871
offset_x = 459405
offset_y = 4432600
ratio = 13.6
p0 = [0, 0, 1]
p1 = [10, 0]
# ---------------------------------------

list_name = []
front_wheel_angle_fitting = []
steering_angle = []

def listdir(list_name, path):
    list_dir = os.listdir(path)
    for file in list_dir:
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1] == ".bag":
            list_name.append(file_path)

def circle_func(p, y, x):
    a, b, r = p
    return pow((np.float64(x) - a),2) + pow((np.float64(y) - b),2) - pow(np.float64(r),2)

def linear_func(p, y, x):
    k, b = p
    return np.float64(y) - (k * np.float64(x) + b)


def curve_fitting(steering_angle, front_wheel_angle, offset_x, offset_y, lfr, p0, topics_name, is_show, file_path):
    bag = rosbag.Bag(file_path)
    front_wheel_angle_tmp = []
    x_gps_tmp = []
    y_gps_tmp = []

    for topic, msg, t in bag.read_messages(topics=topics_name):
        if topic == str('/holo/car_state_hpp'):
            front_wheel_angle_tmp.append(msg.front_wheel_angle)
        if topic == str('/holo/sensors/novatel/odometry'):
            x_gps_tmp.append(msg.pose.position.x - offset_x)
            y_gps_tmp.append(msg.pose.position.y - offset_y)

    average = np.mean(front_wheel_angle_tmp) * 180 / math.pi * ratio
    steering_angle.append(average)

    [lsq_circle, res] = optimize.leastsq(circle_func, p0, args=(y_gps_tmp, x_gps_tmp))
    xc = lsq_circle[0]
    yc = lsq_circle[1]
    rc = lsq_circle[2]

    if res == 5 or res == 6 or res == 7 or res == 8:
        print("LEASTSQ_FAILURE: ", file_path)
        return -1
    else:
        print("LEASTSQ_SUCCESS: ", file_path)

    # print("Circle Center position: ", "xc = ", lsq_circle[0], "yc = ", lsq_circle[1])
    # print("Circle Radius: ", "rc = ", lsq_circle[2])
    # print("Circle Fitting info: ", res)
    # print("--------------------------------------------")

    fw_angle = math.atan(lfr / rc) / math.pi * 180

    if average < 0:
        fw_angle = -math.fabs(fw_angle)
    front_wheel_angle.append(fw_angle)
    print(fw_angle)
    bag.close()

    if is_show == 1:
        alpha = np.linspace(0, 2 * math.pi, 100)
        plt.plot(xc + rc * np.cos(alpha), yc + rc * np.sin(alpha), 'b-.')
        plt.plot(x_gps_tmp, y_gps_tmp, 'r')
        plt.grid()
        plt.axis([-40, 120, 0, 120])

def main(argv):
    bag_path = ''
    is_show = 0

    try:
      opts, args = getopt.getopt(argv, "-h-v",['config_file=','show='])
    except getopt.GetoptError:
        print('please input right params.')
        sys.exit(-1)
    for opt, value in opts:
        if opt in ('-h'):
            print('ident.py  --config_file <bag_path> ---show <0|1>')
            sys.exit(1)
        elif opt in ('-v'):
            print('ident.py version = (1.0)')
            sys.exit(1)
        elif opt in ('--config_file'):
            bag_path = format(value)
        elif opt in ('--show'):
            is_show = int(format(value))

    print("-------- Automatic Transmission Ratio and Bias Calibration Tool --------")
    listdir(list_name, bag_path)

    if is_show == 1:
        plt.figure(1)

    for i in list_name:
        curve_fitting(steering_angle, front_wheel_angle_fitting, offset_x, offset_y, lfr, p0, topics_name, is_show, i)

    if is_show == 1:
        plt.legend(['Fitting point', 'Sample point'])
        plt.xlabel('X position (m)')
        plt.ylabel('Y position (m)')
        plt.title('Fitting Map of Trajectory')

    [lsq_linear, res] = optimize.leastsq(linear_func, p1, args=(steering_angle, front_wheel_angle_fitting))

    if res == 5 or res == 6 or res == 7 or res == 8:
        print("LEASTSQ_FAILURE: Linear equation")
    else:
        print("------------------------------------------------------------------------")
        print("LEASTSQ_SUCCESS: Linear equation")
        print("Transmission Ratio: ", lsq_linear[0])
        print("Steering Angle Bias: ", lsq_linear[1])
        print("------------------------------------------------------------------------")

    if is_show == 1:
        plt.figure(2)
        plt.plot(front_wheel_angle_fitting, steering_angle,'r.')
        plt.plot(front_wheel_angle_fitting, lsq_linear[0]*np.float64(front_wheel_angle_fitting) + lsq_linear[1], 'b')
        plt.legend(['Sample point', 'Fitting point'])
        plt.xlabel('front wheel angle (Deg)')
        plt.ylabel('steer angle (Deg)')
        plt.title('Fitting Map of Transmission Ratio')
        plt.grid()
        plt.show()

if __name__ == '__main__':
    main(sys.argv[1:])