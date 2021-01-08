#!/bin/bash
# 启动decoder和roscore

killall roscore
sleep 1
roscore &
sleep 3

cd /home/holo/workspace_birdview/5987/target
source setup.bash
HOLO_ROOT=/home/holo/workspace_birdview/5987/target

./bin/ros/image_decoder_cmw -c config/holo_sensors/app_config/front_center_camera_gs_app.yaml -n fc_gs &
sleep 2
./bin/ros/image_decoder_cmw -c config/holo_sensors/app_config/front_right_camera_app.yaml -n fr &
sleep 2
./bin/ros/image_decoder_cmw -c config/holo_sensors/app_config/front_left_camera_app.yaml -n fl &
sleep 2
./bin/ros/image_decoder_cmw -c config/holo_sensors/app_config/rear_center_camera_app.yaml -n rc &
