#!/bin/bash
# 启动环视拼接程序

cd /home/holo/workspace_birdview/5987/target
source setup.bash
HOLO_ROOT=/home/holo/workspace_birdview/5987/target

output_path=$1
mkdir -p $output_path

./bin/ros/birdview_splicer_cmw -c config/holo_localization_vision/app_config/birdview/birdview_hpp.yaml -s 1 -o ${output_path}


