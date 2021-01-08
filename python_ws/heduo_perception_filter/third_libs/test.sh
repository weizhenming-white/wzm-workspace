#!/usr/bin/env bash

bag_path=$1
count=`ls ${bag_path}/*.bag | wc -l`
echo $count