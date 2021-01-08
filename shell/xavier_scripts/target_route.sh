#!/bin/bash

# input route_id to mapping
# kill vslam

# change online_mapping/offline_mapping route_id
cd $HOLO_ROOT/config/holo_localization_vision/app_config/vslam &&
route_id=`cat visual_mapping_hpp.yaml | grep -oE "route_.*" | awk -F '"' '{print $1}' | head -n1 | awk -F '_' '{print $2}'` &&
#route_id=`cat vslam_hpp.yaml | grep -oE "route_.*/" | awk -F '/' '{print $1}' | head -n1 | awk -F '_' '{print $2}'` &&
sed -i "s/route_$route_id/route_$1/g" $HOLO_ROOT/config/holo_localization_vision/app_config/vslam/visual_mapping_hpp.yaml && # $HOLO_ROOT/config/holo_localization_vision/lib_config/app/visual_mapping.yaml &&
#sed -i "s/route_$route_id/route_$1/g" vslam_hpp.yaml &&

# change offline mapping route_id
cd $HOLO_ROOT/config/holo_localization_vision/lib_config/app &&
offline_route_id=`cat visual_mapping.yaml | grep -oE "route_.*" | awk -F '"' '{print $1}' | head -n1 | awk -F '_' '{print $2}'` &&
sed -i "s/route_$offline_route_id/route_$1/g" visual_mapping.yaml &&

echo "Route id change to $1"

#echo "Restart vslam"
##sleep 1
# Start vslam
#cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/vslam_cmw -c config/holo_localization_vision/app_config/vslam/visual_localization_hpp.yaml -l 1 -m 0 >/dev/null 2>&1 &
#cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/vslam_cmw -c config/holo_localization_vision/app_config/vslam/vslam_hpp.yaml -l 1 -m 0 >/dev/null 2>&1 &
#sleep 3
