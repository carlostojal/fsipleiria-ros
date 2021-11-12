import rospy
from std_msgs.msg import Float64

class Controls:

    def __init__(self):
        self.throttle_pub = rospy.Publisher('throttle', Float64, queue_size=10)
        rospy.init_node('controls', anonymous=True)

    def clutch(value):
        # set clutch percentage here
        return

    def brake(value):
        # set brake percentage here
        return
    
    def throttle(self, value):
        self.throttle_pub.publish(value)

    def gearUp():
        # gear up
        return

    def gearDown():
        # gear down
        return

    def steering(value):
        # set steering to percentage here
        # 0 -> 1 = right
        # 0 -> -1 = left
        return
