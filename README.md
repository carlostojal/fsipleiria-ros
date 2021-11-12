# fsipleiria-ros

## Requirements

### Hardware 

- A 32 or 64-bit computer.
- A microcontroller (Arduino, ARM Mbed, or Tiva-C Launchpads).
- USB or ethernet link between the computer and the microcontroller.

### Software

- Operating system: Ubuntu 20.04 (Focal)
- ROS Noetic Ninjemys
    - rosservice

## Setup

- Install Ubuntu 20.04 (Focal) on the machine (Either Desktop or Core version. Core is CLI, but has better performance. Can't use ROS 2D/3D visualization). The process is very straightforward and is like installing any other OS.
- Install ROS Noetic Ninjemys. Process described here: http://wiki.ros.org/noetic/Installation/Ubuntu.
- Add the line ```source $FSIPL_ROS_DIR/fsipleiria/devel/setup.sh``` to the end of the ~/.bashrc file, being $FSIPL_ROS_DIR the directory of this root folder.

## Get up and running

- Open a terminal and type the command ```roscore```. This starts the ROS core framework.
- Open a new terminal and type ```catkin_make``` inside the root of this directory.
- Open a new terminal and enter this command, : ```rosrun controls {$NODE_NAME}```, replacing in each time $NODE_NAME by this:
    - brake_listener.py
    - clutch_listener.py
    - gears_listener.py
    - steering_listener.py
    - throttle_listener.py

This is still to be more automated.