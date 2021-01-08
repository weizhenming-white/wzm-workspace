#!/usr/bin/env bash
# 推迟运行

sleep 14400

# first script
cd /home/holo/perception_data_filter/tools; ./start_decoder.sh &
sleep 10

# second script
cd /home/holo/perception_data_filter/tools; ./start_birdview.sh /media/holo/data1/wzm/test_data/birdview_image/zhonghaiguangchang/20201023/ &
sleep 5

# third script
cd /home/holo/perception_data_filter/tools; ./play_bag.sh /home/holo/bags/sport_bag/zhonghaiguangchang/20201023 &

# four script
./monitor.sh
