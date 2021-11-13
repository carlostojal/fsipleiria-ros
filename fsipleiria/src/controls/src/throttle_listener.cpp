#include "ros/ros.h"
#include "std_msgs/Float64.h"

void callback(const std_msgs::Float64::ConstPtr& msg) {
  ROS_INFO("I heard: [%f]", msg->data);
}

int main(int argc, char **argv) {

    // initialize the node
    ros::init(argc, argv, "throttle_listener_cpp");

    // this is the main access point to communications with the ROS system
    ros::NodeHandle n;

    // the second argument is the queue size
    ros::Subscriber sub = n.subscribe("controls/throttle", 1000, callback);

    ros::spin();

    return 0;
}