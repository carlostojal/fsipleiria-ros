# fsipleiria-ros

## Introduction

This is the ROS software for the driverless formula car of the FSIPLeiria team.

## Requirements

### Hardware 

- A 32 or 64-bit computer.

### Software

- Operating system: Ubuntu 20.04 (Focal)
- ROS Noetic Ninjemys

## Setup

- Install Ubuntu 20.04 (Focal) on the machine (Either Desktop or Core version. Core is CLI, but has better performance. Can't use ROS 2D/3D visualization). The process is very straightforward and is like installing any other OS.
- Install ROS Noetic Ninjemys. Process described here: http://wiki.ros.org/noetic/Installation/Ubuntu.
- Add the line ```source $FSIPL_ROS_DIR/fsipleiria/devel/setup.sh``` to the end of the ~/.bashrc file, being $FSIPL_ROS_DIR the directory of this root folder.

## Get up and running

- Open a terminal and type the command ```roscore```. This starts the ROS core framework.
- Open a new terminal and type ```catkin_make``` inside the root of this directory.
- Start the controls package by running ```rosrun controls controls.launch```.

## But how do I control the car?

- Make sure ROS is running by following the instructions on "Get up and running".
- For now, place your code inside the ```Formula``` folder. Otherwise Python won't know where our wonderful modules are.
- Just start coding and use the modules like shown in ```example.py```. Feel free to explore the modules for better understanding.