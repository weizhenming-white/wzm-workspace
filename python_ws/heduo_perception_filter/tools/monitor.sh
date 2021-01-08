#!/bin/bash
# 监控环视拼接导出工具，当不播放bag时，关闭环视拼接程序和decoder程序以及roscore

while :
do
    sleep 3
    DTTERM=`pgrep play_bag.sh`
    if [ -n "$DTTERM" ]
    then
        echo "ready"
    else
        echo "exit birdview node."
        killall birdview_splicer_cmw
        echo "exit decoder node"
        killall image_decoder_cmw
        echo "exit roscore"
        killall roscore
        break
    fi
done
