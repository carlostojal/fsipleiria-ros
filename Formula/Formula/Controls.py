import rospy
from std_msgs.msg import Float64, Int8
from time import sleep    

class Controls:

    def __init__(self, wait_time=0.0):
        print("Initializing controls.")
        # these are the topics that we will be publishing to
        self.throttle_pub = rospy.Publisher('/controls/throttle', Float64, queue_size=10)
        self.clutch_pub = rospy.Publisher('controls/clutch', Float64, queue_size=10)
        self.brake_pub = rospy.Publisher('controls/brake', Float64, queue_size=10)
        self.gears_pub = rospy.Publisher('controls/gears', Int8, queue_size=10)
        self.steering_pub = rospy.Publisher('controls/steering', Float64, queue_size=10)

        # initialize values at zero
        self.current_clutch_value = 0.0
        self.current_brake_value = 0.0
        self.current_throttle_value = 0.0
        self.current_steering_value = 0.0

        # this declares this instance as a rospy node
        rospy.init_node('controls', anonymous=True)
        # sometimes the subscriber is not yet ready to receive messages, so give it some time
        sleep(wait_time)

        print("Controls initialized.")

    def __del__(self):
        print("Unregistering controls.")
        # when class is destroyed (or garbage collected)
        # all publushers are unregistered
        self.throttle_pub.unregister()
        self.clutch_pub.unregister()
        self.brake_pub.unregister()
        self.gears_pub.unregister()
        self.steering_pub.unregister()
        print("Controls unregistered.")

    def clutch(self, value):

        self.current_clutch_value = value
        self.clutch_pub.publish(value)

    def brake(self, value):

        self.current_brake_value = value
        self.brake_pub.publish(value)
    
    def throttle(self, value):
        
        self.current_throttle_value = value
        self.throttle_pub.publish(value)

    def gearUp(self):
        self.gears_pub.publish(1)

    def gearDown(self):
        self.gears_pub.publish(-1)

    def steering(self, value):

        self.current_steering_value = value
        self.steering_pub.publish(value)

        # 0 -> 1 = right
        # 0 -> -1 = left