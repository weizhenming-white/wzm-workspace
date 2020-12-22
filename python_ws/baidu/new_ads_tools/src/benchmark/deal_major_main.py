#!/usr/bin/python
# -*- coding: UTF-8 -*-

import third_libs.deal_rawdata_lib as deal_rawdata_lib
import third_libs.acc_follow_obs_lib as acc_follow_obs_lib
import third_libs.acc_follow_stop_lib as acc_follow_stop_lib


def B_perception_car():
    """
    探测前方车辆距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_car")
    _max_distance = data["autoobs_distance"][0] - 3.8 - 2.4

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_perception_people():
    """
    探测前方行人距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_people")
    _max_distance = data["autoobs_distance"][0] - 3.8 - 0.25

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_perception_bike():
    """
    探测前方自行车距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_bike")
    _max_distance = data["autoobs_distance"][0] - 3.8 - 0.25

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_perception_zhuitong():
    """
    探测前方锥筒距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_zhuitong")
    _max_distance = data["autoobs_distance"][0] - 3.8

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_perception_sanjiaopai():
    """
    探测前方三角牌距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_sanjiaopai")
    _max_distance = data["autoobs_distance"][0] - 3.8

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_perception_shuima():
    """
    探测前方水马距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_perception_shuima")
    _max_distance = data["autoobs_distance"][0] - 3.8

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_rear_perception_car():
    """
    后方探测车辆距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_car_later_speed_10")
    _max_distance = data["autoobs_distance"][0] - 3.8 - 2.4

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_rear_perception_people():
    """
    后方探测行人距离
    产出指标为：展示数据，展示指标
    产出形式：列表
    """
    data = deal_rawdata_lib.read_txt("B_people_later_speed_0.5")
    _max_distance = data["autoobs_distance"][0] - 3.8 - 0.25

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_car_volume():
    """
    处理场景：车辆生命周期识别水平投影
    产出指标有：展示数据（data["volume"]）；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_perception_car")

    # 将障碍物的水平体积保存到data里面，并拿出最大最小值、均值和99分位值

    valid_data = deal_rawdata_lib.basic_index(data["volume"])

    return [data, valid_data]


def B_people_volume():
    """
    处理场景：行人生命周期识别水平投影
    产出指标有：展示数据（data["volume"]）；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_perception_people")

    # 将障碍物的水平体积保存到data里面，并拿出最大最小值、均值和99分位值

    valid_data = deal_rawdata_lib.basic_index(data["volume"])

    return [data, valid_data]


def B_bike_volume():
    """
    处理场景：自行车生命周期识别水平投影
    产出指标有：展示数据（data["volume"]）；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_perception_bike")

    # 将障碍物的水平体积保存到data里面，并拿出最大最小值、均值和99分位值

    valid_data = deal_rawdata_lib.basic_index(data["volume"])

    return [data, valid_data]


def B_zhuitong_volume():
    """
    处理场景：锥筒生命周期识别水平投影
    产出指标有：展示数据（data["volume"]）；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_perception_zhuitong")

    # 将障碍物的水平体积保存到data里面，并拿出最大最小值、均值和99分位值

    valid_data = deal_rawdata_lib.basic_index(data["volume"])

    return [data, valid_data]


def B_shuima_volume():
    """
    处理场景：水马生命周期识别水平投影
    产出指标有：展示数据（data["volume"]）；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_perception_shuima")

    # 将障碍物的水平体积保存到data里面，并拿出最大最小值、均值和99分位值

    valid_data = deal_rawdata_lib.basic_index(data["volume"])

    return [data, valid_data]


def B_perception_car_speed_10():
    """
    处理场景：10km/h车辆速度识别值
    产出指标有：展示数据；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_car_later_speed_10")

    # 将速度转化成千米每小时
    for i in range(len(data["autoobs_obspeed"])):
        data["autoobs_obspeed"][i] = data["autoobs_obspeed"][i] * 3.6

    valid_data = deal_rawdata_lib.basic_index(data["autoobs_obspeed"])

    return [data, valid_data]


def B_perception_car_speed_30():
    """
    处理场景：30km/h车辆速度识别值
    产出指标有：展示数据；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_car_later_speed_30")

    # 将速度转化成千米每小时
    for i in range(len(data["autoobs_obspeed"])):
        data["autoobs_obspeed"][i] = data["autoobs_obspeed"][i] * 3.6

    valid_data = deal_rawdata_lib.basic_index(data["autoobs_obspeed"])

    return [data, valid_data]


def B_perception_car_speed_50():
    """
    处理场景：50km/h车辆速度识别值
    产出指标有：展示数据；展示指标（最大、最小、均值、和99分位值）
    """
    data = deal_rawdata_lib.read_txt("B_car_later_speed_50")

    # 将速度转化成千米每小时
    for i in range(len(data["autoobs_obspeed"])):
        data["autoobs_obspeed"][i] = data["autoobs_obspeed"][i] * 3.6

    valid_data = deal_rawdata_lib.basic_index(data["autoobs_obspeed"])

    return [data, valid_data]


def B_perception_traffic_lights():
    """
    处理场景：第一次开始识别红绿灯距离
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_traffic_stop")
    valid_data = dict()

    # 获取有效的第一次感知到红绿灯的距离
    for i in data["trafficlight_distance"]:
        if i > 0:
            valid_data["max_distance"] = i
            break

    return [data, valid_data]


def B_static_car():
    """
    处理场景：前方静止车辆
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离）
    """
    data = deal_rawdata_lib.read_txt("B_static_car")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 50, 6.2)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]

    return [aeb_data, valid_data]


def B_line_keep():
    """
    处理场景：车道保持：距离道路中心距离；距离中心标准差
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_perception_car")

    value_data = deal_rawdata_lib.basic_index(data["autostatus_keepline"])

    return [data, value_data]


def B_traffic_lights_people():
    """
    处理场景：红灯时人行道有行人停车距离
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_traffic_people_stop")

    _max_distance = data["autoobs_distance"][-1] - 3.8 - 0.25

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_traffic_lights_car():
    """
    处理场景：红灯时人行道有车辆停车距离
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_traffic_obs_stop")

    _max_distance = data["autoobs_distance"][-1] - 3.8 - 2.4

    valid_data = dict()
    valid_data["max_distance"] = _max_distance

    return [data, valid_data]


def B_static_people():
    """
    处理场景：前方静止人
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离）
    """
    data = deal_rawdata_lib.read_txt("B_static_people")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 50, 3.8 + 0.25)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]

    return [aeb_data, valid_data]


def B_static_sanjiaopai():
    """
    处理场景：前方静止三角牌
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离）
    """
    data = deal_rawdata_lib.read_txt("B_static_sanjiaopai")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 50, 3.8)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]

    return [aeb_data, valid_data]


def B_aeb_10():
    """
    处理场景：10km/h刹车
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离和最小ttc）
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_10")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 10, 3.8 + 2.4)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离和最小ttc
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]
    valid_data["min_ttc"] = min(aeb_data["autoobs_ttc"])

    return [aeb_data, valid_data]


def B_aeb_20():
    """
    处理场景：20km/h刹车
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离和最小ttc）
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_20")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 20, 3.8 + 2.4)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离和最小ttc
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]
    valid_data["min_ttc"] = min(aeb_data["autoobs_ttc"])

    return [aeb_data, valid_data]


def B_aeb_30():
    """
    处理场景：30km/h刹车
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离和最小ttc）
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_30")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 30, 3.8 + 2.4)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离和最小ttc
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]
    valid_data["min_ttc"] = min(aeb_data["autoobs_ttc"])

    return [aeb_data, valid_data]


def B_aeb_40():
    """
    处理场景：40km/h刹车
    产出指标有：展示数据；展示指标（开始刹车距离、最大减速度、停车距离和最小ttc）
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_40")

    aeb_data = acc_follow_stop_lib.acc_follow_stop(data, 40, 3.8 + 2.4)

    # 保存指标数据：开始刹车距离、最大减速度、停车距离和最小ttc
    valid_data = dict()
    valid_data["start_brake_distance"] = aeb_data["autoobs_distance"][0]
    valid_data["max_a"] = min(aeb_data["autoobs_auto-a-y"])
    valid_data["stop_distance"] = aeb_data["autoobs_distance"][-1]
    valid_data["min_ttc"] = min(aeb_data["autoobs_ttc"])

    return [aeb_data, valid_data]


def B_acc_10():
    """
    处理场景：10km/h跟车
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_10")

    acc_data = acc_follow_obs_lib.acc_follow_obs(data, 10, 3.8 + 2.4)

    # 加加速度计算方法
    dealwith_distance = list()
    dealwith_timestamp = list()
    gaga_speed_list = list()
    for one in range(1, len(acc_data["autoobs_distance"])):
        dealwith_distance.append(acc_data["autoobs_distance"][one] - acc_data["autoobs_distance"][one - 1])
    for j in range(1, len(acc_data["autoobs_timestamp"])):
        dealwith_timestamp.append(acc_data["autoobs_timestamp"][j] - acc_data["autoobs_timestamp"][j - 1])

    for num in range(len(dealwith_timestamp)):
        try:
            gaga_speed_list.append(dealwith_distance[num] / dealwith_timestamp[num])
        except:
            print u"除数为0"

    # 摆动频率、偏离车道中心线平均距离的计算方法
    sum_dis = 0
    count = 0
    temp = acc_data["autoobs_line-distance"][0]
    for i in range(0, len(acc_data["autoobs_line-distance"])):
        sum_dis = sum_dis + abs(acc_data["autoobs_line-distance"][i])
        if (acc_data["autoobs_line-distance"][i] > 0 and temp < 0) or \
                (acc_data["autoobs_line-distance"][i] < 0 and temp > 0):
            count = count + 1
            temp = acc_data["autoobs_line-distance"][i]
    _hz = count / (acc_data["autoobs_timestamp"][-1] - acc_data["autoobs_timestamp"][0])
    _ave_line_distance = sum_dis / len(acc_data["autoobs_line-distance"])

    # 保存指标数据：平均速度、最小ttc、最小thw、最大加加速度、最大减速度、最大横向加速度、摇摆频率、最大摆动幅度、偏离车道中心线平均距离
    valid_data = dict()
    valid_data["ave_speed"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-speed"])["ave"]
    valid_data["min_ttc"] = deal_rawdata_lib.basic_index(acc_data["autoobs_ttc"])["min"]
    valid_data["min_thw"] = deal_rawdata_lib.basic_index(acc_data["autoobs_thw"])["min"]
    valid_data["max_gaga_speed"] = max(gaga_speed_list)
    valid_data["max_a_y"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-y"])["min"]
    valid_data["max_a_x"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["max"],
                                abs(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["min"]))
    valid_data["hunting_frequency"] = _hz
    valid_data["max_hunt"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["max"],
                                 abs(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["min"]))
    valid_data["ave_line_distance"] = _ave_line_distance

    return [acc_data, valid_data]


def B_acc_30():
    """
    处理场景：30km/h跟车
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_30")

    acc_data = acc_follow_obs_lib.acc_follow_obs(data, 30, 3.8 + 2.4)

    # 加加速度计算方法
    dealwith_distance = list()
    dealwith_timestamp = list()
    gaga_speed_list = list()
    for one in range(1, len(acc_data["autoobs_distance"])):
        dealwith_distance.append(acc_data["autoobs_distance"][one] - acc_data["autoobs_distance"][one - 1])
    for j in range(1, len(acc_data["autoobs_timestamp"])):
        dealwith_timestamp.append(acc_data["autoobs_timestamp"][j] - acc_data["autoobs_timestamp"][j - 1])

    for num in range(len(dealwith_timestamp)):
        try:
            gaga_speed_list.append(dealwith_distance[num] / dealwith_timestamp[num])
        except:
            print u"除数为0"

    # 摆动频率、偏离车道中心线平均距离的计算方法
    sum_dis = 0
    count = 0
    temp = acc_data["autoobs_line-distance"][0]
    for i in range(0, len(acc_data["autoobs_line-distance"])):
        sum_dis = sum_dis + abs(acc_data["autoobs_line-distance"][i])
        if (acc_data["autoobs_line-distance"][i] > 0 and temp < 0) or \
                (acc_data["autoobs_line-distance"][i] < 0 and temp > 0):
            count = count + 1
            temp = acc_data["autoobs_line-distance"][i]
    _hz = count / (acc_data["autoobs_timestamp"][-1] - acc_data["autoobs_timestamp"][0])
    _ave_line_distance = sum_dis / len(acc_data["autoobs_line-distance"])

    # 保存指标数据：平均速度、最小ttc、最小thw、最大加加速度、最大减速度、最大横向加速度、摇摆频率、最大摆动幅度、偏离车道中心线平均距离
    valid_data = dict()
    valid_data["ave_speed"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-speed"])["ave"]
    valid_data["min_ttc"] = deal_rawdata_lib.basic_index(acc_data["autoobs_ttc"])["min"]
    valid_data["min_thw"] = deal_rawdata_lib.basic_index(acc_data["autoobs_thw"])["min"]
    valid_data["max_gaga_speed"] = max(gaga_speed_list)
    valid_data["max_a_y"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-y"])["min"]
    valid_data["max_a_x"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["max"],
                                abs(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["min"]))
    valid_data["hunting_frequency"] = _hz
    valid_data["max_hunt"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["max"],
                                 abs(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["min"]))
    valid_data["ave_line_distance"] = _ave_line_distance

    return [acc_data, valid_data]


def B_acc_40():
    """
    处理场景：40km/h跟车
    产出指标有：展示数据；展示指标
    """
    data = deal_rawdata_lib.read_txt("B_acc_aeb_40")

    acc_data = acc_follow_obs_lib.acc_follow_obs(data, 40, 3.8 + 2.4)

    # 加加速度计算方法
    dealwith_distance = list()
    dealwith_timestamp = list()
    gaga_speed_list = list()
    for one in range(1, len(acc_data["autoobs_distance"])):
        dealwith_distance.append(acc_data["autoobs_distance"][one] - acc_data["autoobs_distance"][one - 1])
    for j in range(1, len(acc_data["autoobs_timestamp"])):
        dealwith_timestamp.append(acc_data["autoobs_timestamp"][j] - acc_data["autoobs_timestamp"][j - 1])

    for num in range(len(dealwith_timestamp)):
        try:
            gaga_speed_list.append(dealwith_distance[num] / dealwith_timestamp[num])
        except:
            print u"除数为0"

    # 摆动频率、偏离车道中心线平均距离的计算方法
    sum_dis = 0
    count = 0
    temp = acc_data["autoobs_line-distance"][0]
    for i in range(0, len(acc_data["autoobs_line-distance"])):
        sum_dis = sum_dis + abs(acc_data["autoobs_line-distance"][i])
        if (acc_data["autoobs_line-distance"][i] > 0 and temp < 0) or \
                (acc_data["autoobs_line-distance"][i] < 0 and temp > 0):
            count = count + 1
            temp = acc_data["autoobs_line-distance"][i]
    _hz = count / (acc_data["autoobs_timestamp"][-1] - acc_data["autoobs_timestamp"][0])
    _ave_line_distance = sum_dis / len(acc_data["autoobs_line-distance"])

    # 保存指标数据：平均速度、最小ttc、最小thw、最大加加速度、最大减速度、最大横向加速度、摇摆频率、最大摆动幅度、偏离车道中心线平均距离
    valid_data = dict()
    valid_data["ave_speed"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-speed"])["ave"]
    valid_data["min_ttc"] = deal_rawdata_lib.basic_index(acc_data["autoobs_ttc"])["min"]
    valid_data["min_thw"] = deal_rawdata_lib.basic_index(acc_data["autoobs_thw"])["min"]
    valid_data["max_gaga_speed"] = max(gaga_speed_list)
    valid_data["max_a_y"] = deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-y"])["min"]
    valid_data["max_a_x"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["max"],
                                abs(deal_rawdata_lib.basic_index(acc_data["autoobs_auto-a-x"])["min"]))
    valid_data["hunting_frequency"] = _hz
    valid_data["max_hunt"] = max(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["max"],
                                 abs(deal_rawdata_lib.basic_index(acc_data["autoobs_line-distance"])["min"]))
    valid_data["ave_line_distance"] = _ave_line_distance

    return [acc_data, valid_data]


if __name__ == '__main__':
    print B_acc_40()[1]
