#!/usr/bin/python
# -*- coding: UTF-8 -*-

import ConfigParser


def get_autostatus_data(path, filename):
    m = 1
    autostatus_key = []
    autostatus_data = {}
    with open(path + filename) as f:
        for row in f:
            if m == 1:
                for i in range(len(row.split())):
                    autostatus_key.append(row.split()[i])
            if m == 1:
                for j in autostatus_key:
                    autostatus_data[j] = list()
            if m != 1:
                for n in range(len(autostatus_key)):
                    autostatus_data[autostatus_key[n]].append(row.split()[n])
            m += 1
    print autostatus_data.keys()
    return autostatus_data


def get_position(path, filename):
    data = get_autostatus_data(path, filename)
    value1 = dict()
    value = dict()
    for key in data.keys():
        value1[key] = list()
        value[key] = list()
    # 起点人行横道坐标
    x_1 = 470792.210
    y_1 = 4399229.353
    x_2 = 470793.989
    y_2 = 4399207.852
    # 人为观测到的碰撞点
    point_x = 470796.280
    point_y = 4399208.213
    # x_3 = 470790.621751
    # y_3 = 4399207.669239
    # x_4 = 470788.973902
    # y_4 = 4399229.227603
    k1 = (y_1 - y_2) / (x_1 - x_2)
    num1 = 0
    for i in range(len(data["position_x"])):
        x = float(data["position_x"][i])
        y = float(data["position_y"][i])
        distance = abs(((k1 * (x - x_1)) - (y - y_1))) / \
                   pow(1 + pow(k1, 2), (1.0 / 2))
        if distance <= 4:
            num1 += 1
        if num1 != 0:
            for j in data.keys():
                value1[j].append(data[j][i])

    distan = list()
    for m in range(len(value1["position_x"])):
        l = pow(pow((point_x - float(value1["position_x"][m])), 2) +
                pow((point_y - float(value1["position_y"][m])), 2), (1.0 / 2))
        distan.append(l)

    global key_x, key_y
    key_x = float(value1["position_x"][distan.index(min(distan))])
    key_y = float(value1["position_y"][distan.index(min(distan))])

    for n in range(len(value1["position_x"])):
        if n <= distan.index(min(distan)):
            for nn in value.keys():
                value[nn].append(value1[nn][n])

    print "原始长度：", len(data["position_x"])
    print "有效数据长度：", len(value["position_x"])
    print "预测碰撞点坐标：", key_x, key_y
    return value


def get_thw(path, filename, outpath):
    value = get_position(path, filename)
    thw_list = list()
    distance = list()
    thw2_list = list()
    valid_data_list = list()
    steer2_list = list()
    timestamp_list = list()

    for i in range(len(value["position_x"]) - 1):
        if i == 0:
            continue
        x0 = float(value["position_x"][i]) - float(value["position_x"][i - 1])
        y0 = float(value["position_y"][i]) - float(value["position_y"][i - 1])
        if (x0 == 0 and y0 != 0) or (x0 != 0 and y0 == 0) or (x0 != 0 and y0 != 0):
            v = abs(((x0 * float(value["speed_x"][i - 1])) +
                     (y0 * float(value["speed_y"][i - 1])))) / \
                pow((pow(x0, 2) + pow(y0, 2)), (1.0 / 2))

            distan = 0
            for m in range(len(value["position_x"]) - 1):
                if m >= i:
                    x1 = float(value["position_x"][m]) - float(value["position_x"][m - 1])
                    y1 = float(value["position_y"][m]) - float(value["position_y"][m - 1])
                    distan = distan + pow(pow(x1, 2) + pow(y1, 2), (1.0 / 2))
            steer2_list.append(float(value["steer"][i]))
            timestamp_list.append(float(value["timestamp"][i]))
            thw_list.append(distan / v)
            thw2_list.append(distan / float(value["speed"][i - 1]))
            distance.append(distan)
            valid_data = list()
            for n in value.keys():
                valid_data.append(value[n][i])
            valid_data_list.append(valid_data)
        if x0 == 0 and y0 == 0:
            continue

    print "thw共有：", len(thw_list)
    file = open("%sthw%s" % (outpath, filename), "w")
    msg = str()
    for ii in value.keys():
        msg = msg + ii + "\t"
    file.write(msg + "distan\t" + "thw\t" + "thw2\n")
    file.close()
    for mm in range(len(thw_list)):
        message = str()
        for nn in valid_data_list[mm]:
            message = message + str(nn) + "\t"
        with open("%sthw%s" % (outpath, filename), "a+") as f:
            f.write(message + str(distance[mm]) + "\t" +
                    str(thw_list[mm]) + "\t" +
                    str(thw2_list[mm]) + "\n")

    valid_steer = list()
    steer_list = list()
    timestamp2_list = list()
    valid_timestamp = list()
    for mmm in range(len(steer2_list)):
        if mmm == len(steer2_list) - 1:
            continue
        if steer2_list[mmm] == steer2_list[mmm + 1]:
            continue
        steer_list.append(steer2_list[mmm])
        timestamp2_list.append(timestamp_list[mmm])
    for xxx in range(len(steer_list)):
        if xxx == 0:
            continue
        valid_timestamp.append(timestamp2_list[xxx])
        valid_steer.append(steer_list[xxx] - steer_list[xxx - 1])

    valid_ttc = str()
    valid_a_y = str()
    valid_gagaspeed = str()
    valid_a_x = str()

    a_y = list()
    gagaspeed_list = list()
    a_x = list()

    for one in range(len(thw_list)):
        if one == 0:
            continue
        if thw_list[one] < thw_list[one - 1] and thw_list[one] < thw_list[one + 1]:
            valid_ttc = str(thw_list[one])
            break
    for two in range(len(valid_data_list)):
        a_y.append(float(valid_data_list[two][value.keys().index("a_y")]))
        a_x.append(abs(float(valid_data_list[two][value.keys().index("a_x")])))
        if two > 0:
            a = float(valid_data_list[two][value.keys().index("a_y")]) - \
                float(valid_data_list[two - 1][value.keys().index("a_y")])
            time = float(valid_data_list[two][value.keys().index("timestamp")]) - \
                   float(valid_data_list[two - 1][value.keys().index("timestamp")])
            gagaspeed = a / time
            gagaspeed_list.append(gagaspeed)

    count = 0
    max_steer = list()
    print len(valid_steer)
    for three in range(len(valid_steer)):
        if three == len(valid_steer) - 1:
            continue
        for aaa in range(len(valid_timestamp)):
            total = 0
            if valid_timestamp[three] + 1 >= valid_timestamp[aaa] >= valid_timestamp[three]:
                if ((valid_steer[three] > 0) and (valid_steer[three + 1] < 0)) or (
                        (valid_steer[three] < 0) and (valid_steer[three + 1] > 0)):
                    total += 1
            max_steer.append(total)

        if ((valid_steer[three] > 0) and (valid_steer[three + 1] < 0)) or (
                (valid_steer[three] < 0) and (valid_steer[three + 1] > 0)):
            count += 1
    fre_steer = count / (timestamp_list[-1] - timestamp_list[1])

    valid_a_y = str(min(a_y))
    valid_gagaspeed = "%.6f" % round(max(gagaspeed_list), 4)
    valid_a_x = str(max(a_x))
    mess = "无人车与假设碰撞点之间的ttc：\t" + valid_ttc + "\n" \
           + "无人车最大减速度：\t" + valid_a_y + "\n" \
           + "无人车最大加加速度：\t" + valid_gagaspeed + "\n" \
           + "无人车最大横向加速度：\t" + valid_a_x + "\n" \
           + "无人车抖动频率：\t" + str(fre_steer) + "\n" \
           + "单位时间内抖动最大值：\t" + str(max(max_steer)) + "\n" \
           + "无人车一共抖动次数：\t" + str(count)
    print mess
    outfile = open("%sresult%s" % (outpath, filename), "w")
    outfile.write(mess)
    outfile.close()


if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    cf.read("./conf/turn.ini")
    for i in range(len(cf.get("raw_data", "right_turn_filename").split(","))):
        print "start deal with file name is " + cf.get("raw_data", "right_turn_filename").split(",")[i]
        print "\n\n===========================================\n\n"
        try:
            get_thw(cf.get("raw_data", "path"),
                    cf.get("raw_data", "right_turn_filename").split(",")[i],
                    cf.get("out_path", "path"))
        except:
            print "fail"


