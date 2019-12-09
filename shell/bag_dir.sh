#!/bin/sh
first_dir=`date +%Y%m%d`
second_dir=`date +%p`
mkdir -p /home/holo/bags/$first_dir/$second_dir
echo "完成！！"
