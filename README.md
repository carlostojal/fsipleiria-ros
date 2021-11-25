# fsipleiria-ros

## Introduction

This is the ROS software for the driverless formula car of the FSIPLeiria team.

## Functional overview

The custom Python libraries provide a way to communicate with the car.\
The libraries communicate with ROS, that communicate with the electronic units via CAN bus.\
The most recent frame of each ID is stored on a cache server (RAM memory) (Redis Server).

## Requirements

### Hardware 

- A 32 or 64-bit computer.

### Software

- Operating system: Ubuntu 20.04 (Focal)
- ROS Noetic Ninjemys
- Redis Server

## Setup

- Install Ubuntu 20.04 (Focal) on the machine (Either Desktop or Core version. Core is CLI, but has better performance. Can't use ROS 2D/3D visualization). The process is very straightforward and is like installing any other OS.
- Install ROS Noetic Ninjemys. Process described here: http://wiki.ros.org/noetic/Installation/Ubuntu.
- Add the line ```source $FSIPL_ROS_DIR/fsipleiria/devel/setup.sh``` to the end of the ~/.bashrc file, being $FSIPL_ROS_DIR the directory of this root folder.

## Get up and running

- Before starting, set the environment variables REDIS_HOST, REDIS_PORT and REDIS_DB on your OS.
- Open a terminal and type the command ```roscore```. This starts the ROS core framework.
- Open a new terminal and type ```catkin_make``` inside the "fsipleiria" directory.
- Start the controls package by running ```roslaunch controls controls.launch```.

## But how do I control the car?

- Make sure ROS is running by following the instructions on "Get up and running".
- For now, place your code inside the ```Formula``` folder. Otherwise Python won't know where our wonderful modules are.
- Just start coding and use the modules like shown in ```example.py```. Feel free to explore the modules for better understanding.