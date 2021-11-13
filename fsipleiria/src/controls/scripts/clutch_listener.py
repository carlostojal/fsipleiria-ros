import rospy
from std_msgs.msg import Float64

def callback(data):

    clutch_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", clutch_value)

    # use here clutch_value to control clutch actuator



def listener():

    rospy.init_node('clutch_listener', anonymous=True)

    rospy.Subscriber("controls/clutch", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()