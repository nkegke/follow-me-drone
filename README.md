# YOLOv3-based follow-me drone application in ROS

## Usage

* Launch ROS, Gazebo world
```console
$ roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```

* Set drone position
```console
$ ./enable_motors.sh
```
<img src="https://github.com/nkegke/files/blob/main/follow/set1.png" alt="set1" style="width: 15vw;"/> <img src="https://github.com/nkegke/files/blob/main/follow/set2.png" alt="set2" style="width: 15vw;"/>
<img src="https://github.com/nkegke/files/blob/main/follow/set3.png" alt="set3" style="width: 15vw;"/> <img src="https://github.com/nkegke/files/blob/main/follow/set4.png" alt="set4" style="width: 15vw;"/>

* Start Darknet YOLOv3
```console
$ roslaunch darknet_ros darknet_ros.launch
```
<img src="https://github.com/nkegke/files/blob/main/follow/yolo.png" alt="yolo" style="width: 30vw;"/>

* Follow-me simulation
```console
$ python yollow.py
```
<img src="https://github.com/nkegke/files/blob/main/follow/start1.png" alt="start1" style="width: 15vw;"/> <img src="https://github.com/nkegke/files/blob/main/follow/start2.png" alt="start2" style="width: 15vw;"/>
<img src="https://github.com/nkegke/files/blob/main/follow/start3.png" alt="start3" style="width: 15vw;"/> <img src="https://github.com/nkegke/files/blob/main/follow/start4.png" alt="start4" style="width: 15vw;"/>

## Prerequisites

* Ubuntu 18.04 LTS
* NVIDIA GPU

## Setup

### ROS, Darknet, CUDA Installation

```console
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt install curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
$ sudo rosdep init
$ rosdep update
$ mkdir ~/catkin_ws
$ cd ~/catkin_ws
$ wstool init src https://raw.github.com/tu-darmstadt-ros-pkg/hector_quadrotor/kinetic-devel/tutorials.rosinstall
$ sudo apt-get install ros-melodic-geographic-info
$ sudo apt-get install ros-melodic-ros-control
$ sudo apt-get install ros-melodic-gazebo-ros-control
$ sudo apt-get install ros-melodic-joy
$ sudo apt-get install ros-melodic-teleop-twist-keyboard
$ sudo apt install qt4-default
$ cd ~/catkin_ws/src
$ git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
$ cd ../
$ sudo apt update
$ sudo apt install nvidia-cuda-toolkit
$ catkin_make -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/usr/bin/gcc-6
$ echo -e "source ~/catkin_ws/devel/setup.bash" >> .bashrc
```

### Copy (and overwrite) below files in respective directories:

* darknet_ros.launch: ```~/catkin_ws/src/darknet_ros/darknet_ros/launch/```

* ros.yaml: ```~/catkin_ws/src/darknet_ros/darknet_ros/config/```

* act.world: ```~/catkin_ws/src/hector_gazebo/hector_gazebo_worlds/world```

* start.launch: ```~/catkin_ws/src/hector_gazebo/hector_gazebo_worlds/launch```
	
* outdoor_flight_gazebo.launch: ```~/catkin_ws/src/hector_quadrotor/hector_quadrotor_demo/launch```

* quadrotor_downward_cam.gazebo.xacro: ```~/catkin_ws/src/hector_quadrotor/hector_quadrotor_description/urdf/```

* quadrotor_downward_cam.urdf.xacro: ```~/catkin_ws/src/hector_quadrotor/hector_quadrotor_description/urdf/```
	
* walk.dae: ```~/catkin_ws/src/hector_gazebo/hector_gazebo_worlds/world```

* moonwalk.dae: ```~/catkin_ws/src/hector_gazebo/hector_gazebo_worlds/world```
	
