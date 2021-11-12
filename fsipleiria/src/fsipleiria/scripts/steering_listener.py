import rospy
from std_msgs.msg import Float64

def callback(data):

    steering_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", steering_value)

    # use here steering_value to control brake actuator



def listener():

    rospy.init_node('steering_listener', anonymous=True)

    rospy.Subscriber("controls/steering", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()