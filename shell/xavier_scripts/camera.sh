#!/bin/bash
#2019-09-11

# start system route and system time
sudo route add default gw 192.168.1.180
# sudo route add -net 192.168.30.0/24 gw 192.168.1.199
sudo ntpdate cn.pool.ntp.org
sudo hwclock --systohc

#sleep 3

roscore	 &
sleep 3

cd $HOLO_ROOT; source $HOLO_ROOT/setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_sync_cmw --config_file config/holo_sensors/app_config/camera_sync_app.yaml --node_name camera_sync_node & #>/dev/null 2>&1 

cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/front_center_camera_app.yaml --node_name front &  #>/dev/null 2>&1 
#cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/front_fisheye_camera_app.yaml --node_name front_fisheye &
sleep 3
cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/front_center_camera_app.yaml --node_name com_front & #>/dev/null 2>&1 &
#cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/front_fisheye_camera_app.yaml --node_name front_h264 &

# start perception node (GPU)
# sleep 5

#cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/vision_freespace_app_cmw -c config/holo_perception/app_config/vision_freespace_app.yaml -m 0 >/dev/null 2>&1 &

#cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/camera_obstacle_detection_parking_app_cmw -c config/holo_perception/app_config/camera_obstacle_detection_parking.yaml >/dev/null 2>&1 &




#/home/nvidia/holo_ws/output/native/relwithdebinfo/bin/ros/image_capture_cmw --config_file /home/nvidia/holo_ws/output/native/relwithdebinfo/config/holo_sensors/app_config/rear_center_camera_app.yaml --node_name rear &

#/home/nvidia/holo_ws/output/native/relwithdebinfo/bin/ros/image_encoder_xavier_cmw --config_file /home/nvidia/holo_ws/output/native/relwithdebinfo/config/holo_sensors/app_config/rear_center_camera_app.yaml --node_name com_rear &
#Setup="source /opt/ros/melodic/setup.bash"
#if grep -q ^$Setup$ ~/.bashrc
#then
#    echo "setup.bash in .bashrc is not configured..."
#else
#    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
#source ~/.bashrc
#`fi


