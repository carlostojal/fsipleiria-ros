FROM ros:noetic

# update the system
RUN apt-get update; apt-get -y upgrade
RUN apt-get install -y python3-pip

# create the ROS workspace
RUN mkdir -p /home/catkin_ws/src
COPY ./src /home/catkin_ws/src
COPY ./requirements.txt /home/catkin_ws/requirements.txt
COPY ./docker_entrypoint.sh /home/catkin_ws/docker_entrypoint.sh
WORKDIR /home/catkin_ws

# install dependencies
RUN rosdep update
RUN rosdep install --from-paths src --ignore-src -r -y

RUN pip3 install -r requirements.txt

# build the workspace
RUN . /opt/ros/noetic/setup.sh; catkin_make

# setup environment
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "source ./devel/setup.bash" >> ~/.bashrc

# on container start run this script
ENTRYPOINT [ "./docker_entrypoint.sh" ]