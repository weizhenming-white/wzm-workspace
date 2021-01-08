#!/bin/bash
#2019-09-11
#roscore	&
#sleep 3

#cd $HOLO_ROOT; source $HOLO_ROOT/setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_sync_cmw --config_file config/holo_sensors/app_config/camera_sync_app.yaml --node_name camera_sync_node &

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/front_fisheye_camera_app.yaml --node_name front_fisheye &
sleep 5

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/rear_fisheye_camera_app.yaml --node_name rear_fisheye &
sleep 5

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/left_fisheye_camera_app.yaml --node_name left_fisheye &
sleep 5

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_capture_cmw --config_file config/holo_sensors/app_config/right_fisheye_camera_app.yaml --node_name right_fisheye &
sleep 5 

# encode camera h264
cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/front_fisheye_camera_app.yaml --node_name front_h264 &
sleep 3

cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/rear_fisheye_camera_app.yaml --node_name rear_h264 &

sleep 3
cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/left_fisheye_camera_app.yaml --node_name left_h264 &

sleep 3
cd $HOLO_ROOT ;source setup.bash; HOLO_ROOT=$PWD ./bin/ros/image_encoder_xavier_cmw --config_file config/holo_sensors/app_config/right_fisheye_camera_app.yaml --node_name right_h264 &



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


