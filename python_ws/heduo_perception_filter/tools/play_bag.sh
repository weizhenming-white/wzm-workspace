#!/bin/bash
# 批量按照环视拼接要求播放bag
# use：source export_data.sh ${raw_path}

bag_path=$1

for fn_full in $(ls ${bag_path}/*.bag)
do
    echo "Start play $fn_full"
    rosbag play $fn_full /holo/sensors/camera/front_center_gs_counter:=/drop/gs /holo/sensors/camera/rear_center_counter:=/drop/rc /holo/sensors/camera/front_left_counter:=/drop/fl /holo/sensors/camera/front_right_counter:=/drop/fr

done

