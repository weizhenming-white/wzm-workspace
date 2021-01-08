#!/bin/bash
#2020-11-30

sudo route add default gw 192.168.1.180
sudo ntpdate cn.pool.ntp.org
sudo hwclock --systohc

cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/front_cen    ter_camera_app.yaml --node_name com_front &
sleep 1

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/front_fisheye_camera_app.yaml --node_name front_h264 &
sleep 1

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/rear_fisheye_camera_app.yaml --node_name rear_h264 &
 
sleep 1
cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/left_fisheye_camera_app.yaml --node_name left_h264 & 
sleep 1
cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/right_fisheye_camera_app.yaml --node_name right_h264 &
