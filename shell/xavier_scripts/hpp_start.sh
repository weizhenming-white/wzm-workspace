#!/bin/bash
cd $HOLO_ROOT; source setup.bash; rosservice call /hpp_start "command: $1"
