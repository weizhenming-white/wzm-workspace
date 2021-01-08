#!/bin/bash


cd $HOLO_ROOT; source setup.bash; HOLO_ROOT=$PWD ./bin/ros/vslam_cmw -c config/holo_localization_vision/app_config/vslam/vslam_hpp.yaml &
