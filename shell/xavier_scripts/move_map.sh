#!/bin/bash

path=$HOLO_ROOT/config/holo_localization_vision/vslam
# echo $path

file_name=`date +%F-%H-%M-%S`
date=`date`

if [ -d "/opt/holo/hpp/route_$1" ]
then
#    file_name=`date +%F-%H-%M-%S`
#    date=`date`
    echo "This filder is exist!!!"
    mv /opt/holo/hpp/route_$1 /opt/holo/hpp/route_$1-$file_name
    echo "modify the original file name to route_$1-$file_name"
    # mkdir /opt/holo/hpp/route_$1
    # mv $path/frames.bin $path/mappoints.bin $path/pcd.ply $path/vehicle_odometry.txt $path/front_wheel_angle.txt /opt/holo/hpp/route_$1
	rm -r $path/route_$1/features
	mv $path/route_$1 /opt/holo/hpp
    echo "Create mapping time is $file_name" >/opt/holo/hpp/route_$1/1.txt
else
    echo "Create route_$1 folder"
    # mkdir /opt/holo/hpp/route_$1
    # mv $path/frames.bin $path/mappoints.bin $path/pcd.ply $path/vehicle_odometry.txt $path/front_wheel_angle.txt /opt/holo/hpp/route_$1
	rm -r $path/route_$1/features
 	mv $path/route_$1 /opt/holo/hpp
    echo "Create mapping time is $file_name" >/opt/holo/hpp/route_$1/1.txt
fi
