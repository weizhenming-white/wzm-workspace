#!/usr/bin/env sh
# rosbag record and car ID

msg=`date "+%F-%H-%M-%S_$1"`
#if [$1 ]
rosbag record -aO "$msg.bag"

