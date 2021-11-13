import rospy
from std_msgs.msg import Float64

def callback(data):

    brake_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", brake_value)

    # use here brake_value to control brake actuator



def listener():

    rospy.init_node('brake_listener', anonymous=True)

    rospy.Subscriber("controls/brake", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()