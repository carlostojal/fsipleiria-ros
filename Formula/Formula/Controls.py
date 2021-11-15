import threading
import rospy
from std_msgs.msg import Float64, Int8
from enum import Enum
from time import sleep
import datetime
from threading import Thread
import multiprocessing

# smaller this value, more gradual will be value changes
# with the compromise of worse performance

class AvailableControls(Enum):
    """
    Enum of available controls
    """
    None_ = 0
    Throttle = 1
    Clutch = 2
    Brake = 3
    Gears = 4
    Steering = 5
    

class Controls:

    STEP_TIME = 1

    def __init__(self, wait_time=0.0):
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

        # this is used to stop threads already started
        # ex: car was instructed to steer left, but meanwhile is instructed to steer right
        # in this case, the thread that was started to steer left will be stopped
        self.current_steering_thread = None
        self.stop_steering_thread = False

        # this declares this instance as a rospy node
        rospy.init_node('controls', anonymous=True)
        # sometimes the subscriber is not yet ready to receive messages, so give it some time
        sleep(wait_time)

    def __del__(self):
        # when class is destroyed (or garbage collected)
        # all publushers are unregistered
        self.throttle_pub.unregister()
        self.clutch_pub.unregister()
        self.brake_pub.unregister()
        self.gears_pub.unregister()
        self.steering_pub.unregister()

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

    def steering(self, value, time=0.0):

        if time != 0.0:
            thread = Thread(target=self.gradual_value_update, args=(value, time, AvailableControls.Steering))
            thread.start()
        else:
            self.current_steering_value = value
            self.steering_pub.publish(value)

        # 0 -> 1 = right
        # 0 -> -1 = left

    def gradual_value_update(self, target_value, time, control=AvailableControls.None_):

        if control == AvailableControls.Steering:

            if self.current_steering_thread is not None:
                if self.current_steering_thread.is_alive():
                    # wait for the existing thread to finish
                    # (in the future it is a better idea to finish the thread)
                    self.stop_steering_thread = True
                    self.current_steering_thread.join()

            self.current_steering_thread = threading.current_thread()
            
            val_diff = target_value - self.current_steering_value
        else:
            print("Control not available.")
            return
        
        # number of steps it takes to change value
        n_steps = time / self.STEP_TIME

        for step in range(int(n_steps)):
            if control == AvailableControls.Steering:
                if self.stop_steering_thread:
                    self.stop_steering_thread = False
                    return
                self.current_steering_value = self.current_steering_value + (val_diff / n_steps)
                self.steering_pub.publish(self.current_steering_value)
            else:
                print("Control not available.")
                return
            
            sleep(self.STEP_TIME)
