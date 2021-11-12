import rospy
from std_msgs.msg import Int8

def callback(data):

    gear_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", gear_value)

    # 1 -> gear up
    # -1 -> gear down



def listener():

    rospy.init_node('gears_listener', anonymous=True)

    rospy.Subscriber("controls/gears", Int8, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()