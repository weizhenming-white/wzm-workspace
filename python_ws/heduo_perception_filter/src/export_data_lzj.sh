#!/bin/bash

cd /home/holo/workspace/hpp_20201104/target
source setenv.bash
#/native/relwithdebinfo
#cd /home/lzjever/myworks/pp_data_tools/tools/holo_bin
bags_path=/media/holo/data1/workspace_test/bags/jizhi_tmp/
exports_path=/media/holo/data1/workspace_test/perception_data/raw_data/jizhi
#bags_path=/data/parking_data/demo
#exports_path=/data/parking_data/demo/export


for fn_full in $(ls ${bags_path}/*.bag)
do
    filename=`basename -s .bag $fn_full`
    mkdir -p ${exports_path}/${filename}
    bag_file=${bags_path}/${filename}.bag
    output_path=${exports_path}/${filename}

    ./bin/ros/export_3d_data_cmw -i ${bag_file} --camera_yaml_path config/holo_data_provider/app_config/camera_hpp.yaml -o ${output_path}/camera --output_camera_image 1;


done

cd /home/holo/perception_data_filter/source
