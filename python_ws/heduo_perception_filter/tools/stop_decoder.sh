#!/bin/bash
# 结束decoder和roscore

killall roscore
echo "stop roscore............."
sleep 1
killall image_decoder_cmw
echo "stop decoder................"
sleep 1
