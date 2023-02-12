#!/bin/bash

rosservice call /gazebo/reset_world

echo "Enabling motors..."
rosservice call /enable_motors "enable: true"

echo""
echo "Taking off in:"
echo "3"
sleep 1
echo "2"
sleep 1
echo "1"
sleep 1
./set.py