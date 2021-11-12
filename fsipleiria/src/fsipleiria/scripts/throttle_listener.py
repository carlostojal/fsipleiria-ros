import rospy
from std_msgs.msg import Float64

def callback(data):

    throttle_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", throttle_value)

    # use here throttle_value to control throttle actuator



def listener():

    rospy.init_node('throttle_listener', anonymous=True)

    rospy.Subscriber("controls/throttle", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()