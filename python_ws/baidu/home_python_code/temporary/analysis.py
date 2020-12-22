#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json


def read_70log():
    filename = "dudrive_gateway.log.20180627-151306.3125.json,dudrive_gateway.log.20180627-153529.3125.json"
    mkz70_data = []
    for i in range(len(filename.split(","))):
        with open(r"data\%s" % filename.split(",")[i]) as f:
            data = json.loads(f.read())
            for num in range(len(data)):
                timestamp = data[str(num)]["timestamp"]
                linear_velocity = data[str(num)]["linear_velocity"]
                position = data[str(num)]["position"]
                linear_acceleration = data[str(num)]["linear_acceleration"]
                a_y = str(linear_acceleration).split(" ")[4]
                mkz70_data.append([timestamp, linear_velocity, position, a_y])
    return mkz70_data


def read_68log():
    filename = "dudrive_gateway.log.20180627-152531.2989.json"
    mkz68_data = []
    with open(r"data\%s" % filename) as f:
        data = json.loads(f.read())
        for num in range(len(data)):
            timestamp = data[str(num)]["timestamp"]
            linear_velocity = data[str(num)]["linear_velocity"]
            position = data[str(num)]["position"]
            linear_acceleration = data[str(num)]["linear_acceleration"]
            a_y = str(linear_acceleration).split(" ")[4]
            mkz68_data.append([timestamp, linear_velocity, position, a_y])
    return mkz68_data


def analysis():
    mkz70_data = read_70log()
    mkz68_data = read_68log()
    filename = open(r"output\result_aeb-30-5.txt", "w")
    filename.write("timestamp\t" + "auto_speed\t" + "auto_speed_x\t" +
                   "auto_speed_y\t" + "obs_speed\t" + "obs_speed_x\t" +
                   "obs_speed_y\t" + "distance\t" + "auto_a_y\t" + "obs_a_y\n")
    filename.close()

    timestamp_list = []
    with open(r"data\aeb-15-4.txt") as f:
        for line in f:
            if line.split()[0] == "timestamp":
                continue
            timestamp_list.append(float(line.split()[0]))

    mkz70_result = []
    mkz68_result = []
    for timestamp in timestamp_list:

        for one_data in mkz70_data:
            if float(one_data[0]) == timestamp:
                mkz70_result.append(one_data)
                print "mkz70", one_data

        middle_timestamp = []
        middle_data = []
        for i in mkz68_data:
            if (timestamp - 2) <= float(i[0]) <= (timestamp + 2):
                middle_timestamp.append(float(i[0]))
                middle_data.append(i)
        middle_timestamp.append(timestamp)
        middle_timestamp.sort()
        if min(middle_timestamp) == timestamp:
            for ii in middle_data:
                if float(ii[0]) == middle_timestamp[1]:
                    mkz68_result.append(ii)
                    print "mkz68", ii
                    break
            continue
        if max(middle_timestamp) == timestamp:
            for ii in middle_data:
                if float(ii[0]) == middle_timestamp[len(middle_timestamp) - 2]:
                    mkz68_result.append(ii)
                    print "mkz68", ii
                    break
            continue
        if (timestamp - middle_timestamp[middle_timestamp.index(timestamp) - 1]) > (
                middle_timestamp[middle_timestamp.index(timestamp) + 1] - timestamp):
            for ii in middle_data:
                if float(ii[0]) == middle_timestamp[middle_timestamp.index(timestamp) + 1]:
                    mkz68_result.append(ii)
                    print "mkz68", ii
                    break
            continue
        if (timestamp - middle_timestamp[middle_timestamp.index(timestamp) - 1]) < (
                middle_timestamp[middle_timestamp.index(timestamp) + 1] - timestamp):
            for ii in middle_data:
                if float(ii[0]) == middle_timestamp[middle_timestamp.index(timestamp) - 1]:
                    mkz68_result.append(ii)
                    print "mkz68", ii
                    break
            continue

    print len(mkz70_result)
    print len(mkz68_result)

    for mes in range(len(mkz70_result)):
        try:
            auto_speed = pow(((float(str(mkz70_result[mes][1]).split(" ")[2]) ** 2) +
                              (float(str(mkz70_result[mes][1]).split(" ")[4]) ** 2)), (1.0 / 2))
            obs_speed = pow(((float(str(mkz68_result[mes][1]).split(" ")[2]) ** 2) +
                             (float(str(mkz68_result[mes][1]).split(" ")[4]) ** 2)), (1.0 / 2))
            x = (float(str(mkz70_result[mes][2]).split(" ")[2]) - float(str(mkz68_result[mes][2]).split(" ")[2])) ** 2
            y = (float(str(mkz70_result[mes][2]).split(" ")[4]) - float(str(mkz68_result[mes][2]).split(" ")[4])) ** 2
            distance = pow((x + y), (1.0 / 2))
            message = str(mkz70_result[mes][0]) + "\t" \
                      + str(auto_speed) + "\t" \
                      + str(float(str(mkz70_result[mes][1]).split(" ")[2])) + "\t" \
                      + str(float(str(mkz70_result[mes][1]).split(" ")[4])) + "\t" \
                      + str(obs_speed) + "\t" \
                      + str(float(str(mkz68_result[mes][1]).split(" ")[2])) + "\t" \
                      + str(float(str(mkz68_result[mes][1]).split(" ")[4])) + "\t" \
                      + str(distance) + "\t" \
                      + str(mkz70_result[mes][3]) + "\t" \
                      + str(mkz68_result[mes][3]) + "\n"
            with open(r"output\result_aeb-30-5.txt", "a+") as ff:
                ff.write(message)
        except:
            print "Fail"


analysis()





