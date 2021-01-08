#!/bin/bash

#roscore	&

cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/boot_parking_vehicle_cmw -c config/holo_sys/app_config/boot_parking/boot_parking_vehicle_hpp.yaml -n hpp_parking
#bash source.sh &&
#echo "source finish!!!"
#sleep 3
#`cd ~/holo_ws/output/native/relwithdebinfo/target; HOLO_ROOT=$PWD ./bin/ros/boot_parking_vehicle_cmw -c config/holo_sys/app_config/boot_parking/boot_parking_vehicle_hpp.yaml -n hpp_parking`
#HOLO_ROOT=$PWD ./bin/ros/boot_parking_vehicle_cmw -c config/holo_sys/app_config/boot_parking/boot_parking_vehicle_hpp.yaml -n hpp_parking
