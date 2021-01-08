#!/bin/bash
cd $HOLO_ROOT; source setup.bash; rostopic pub /holo/planning/recovery std_msgs/UInt32 "data: 1" 
