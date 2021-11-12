import rospy
from std_msgs.msg import Float64

class Controls:

    def __init__(self):
        # these are the topics that we will be publishing to
        self.throttle_pub = rospy.Publisher('/controls/throttle', Float64, queue_size=10)
        self.clutch_pub = rospy.Publisher('controls/clutch', Float64, queue_size=10)
        self.brake_pub = rospy.Publisher('controls/brake', Float64, queue_size=10)
        self.gears_pub = rospy.Publisher('controls/gears', Float64, queue_size=10)
        self.steering_pub = rospy.Publisher('controls/steering', Float64, queue_size=10)
        # this declares this instance as a rospy node
        rospy.init_node('controls', anonymous=True)

    def clutch(self, value):
        self.clutch_pub.publish(value)        

    def brake(self, value):
        self.brake_pub.publish(value)
    
    def throttle(self, value):
        self.throttle_pub.publish(value)

    def gearUp(self):
        self.gears_pub.publish(1)

    def gearDown(self):
        self.gears_pub.publish(-1)

    def steering(self, value):
        self.steering_pub.publish(value)
        # 0 -> 1 = right
        # 0 -> -1 = left
