import threading
import rospy
from std_msgs.msg import Float64, Int8
from enum import Enum
from time import sleep
from threading import Thread

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

    # smaller this value, more gradual will be value changes
    # with the compromise of worse performance
    STEP_LEN = 0.01

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

        # this is used to stop threads already started
        # ex: car was instructed to steer left, but meanwhile is instructed to steer right
        # in this case, the thread that was started to steer left will be stopped
        self.current_steering_thread = None
        self.current_throttle_thread = None
        self.current_brake_thread = None
        self.current_clutch_thread = None

        self.stop_steering_thread = False
        self.stop_throttle_thread = False
        self.stop_brake_thread = False
        self.stop_clutch_thread = False

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

    def clutch(self, value, update_time=0.0):

        if update_time != 0.0:
            thread = Thread(target=self.gradual_value_update, args=(value, update_time, AvailableControls.Clutch))
            thread.start()
        else:
            self.current_clutch_value = value
            self.clutch_pub.publish(value)

    def brake(self, value, update_time=0.0):

        if update_time != 0.0:
            thread = Thread(target=self.gradual_value_update, args=(value, update_time, AvailableControls.Brake))
            thread.start()
        else:
            self.current_brake_value = value
            self.brake_pub.publish(value)
    
    def throttle(self, value, update_time=0.0):
        
        if update_time != 0.0:
            thread = Thread(target=self.gradual_value_update, args=(value, update_time, AvailableControls.Throttle))
            thread.start()
        else:
            self.current_throttle_value = value
            self.throttle_pub.publish(value)

    def gearUp(self):
        self.gears_pub.publish(1)

    def gearDown(self):
        self.gears_pub.publish(-1)

    def steering(self, value, update_time=0.0):

        if update_time != 0.0:
            thread = Thread(target=self.gradual_value_update, args=(value, update_time, AvailableControls.Steering))
            thread.start()
        else:
            self.current_steering_value = value
            self.steering_pub.publish(value)

        # 0 -> 1 = right
        # 0 -> -1 = left

    def gradual_value_update(self, target_value, update_time, control=AvailableControls.None_):

        if control == AvailableControls.Steering:

            if self.current_steering_thread is not None and self.current_steering_thread.is_alive():
                self.stop_steering_thread = True
                # have to wait for the existing thread (it will stop, we are just waiting that)
                self.current_steering_thread.join()

            self.current_steering_thread = threading.current_thread()

            val_diff = target_value - self.current_steering_value

        elif control == AvailableControls.Throttle:

            if self.current_throttle_thread is not None and self.current_throttle_thread.is_alive():
                self.stop_throttle_thread = True

            self.current_throttle_thread = threading.current_thread()

            val_diff = target_value - self.current_throttle_value

        elif control == AvailableControls.Brake:

            if self.current_brake_thread is not None and self.current_brake_thread.is_alive():
                self.stop_brake_thread = True

            self.current_brake_thread = threading.current_thread()

            val_diff = target_value - self.current_brake_value

        elif control == AvailableControls.Clutch:

            if self.current_clutch_thread is not None and self.current_clutch_thread.is_alive():
                self.stop_clutch_thread = True

            self.current_clutch_thread = threading.current_thread()

            val_diff = target_value - self.current_clutch_value

        else:
            raise Exception("Control not available." + str(control))
        
        # number of steps it takes to change value
        n_steps = abs(val_diff) / self.STEP_LEN


        for step in range(int(n_steps)):
            if control == AvailableControls.Steering:
                if self.stop_steering_thread:
                    self.stop_steering_thread = False
                    return
                self.current_steering_value = self.current_steering_value + (val_diff / n_steps)
                self.steering_pub.publish(self.current_steering_value)
            elif control == AvailableControls.Throttle:
                if self.stop_throttle_thread:
                    self.stop_throttle_thread = False
                    return
                self.current_throttle_value = self.current_throttle_value + (val_diff / n_steps)
                self.throttle_pub.publish(self.current_throttle_value)
            elif control == AvailableControls.Brake:
                if self.stop_brake_thread:
                    self.stop_brake_thread = False
                    return
                self.current_brake_value = self.current_brake_value + (val_diff / n_steps)
                self.brake_pub.publish(self.current_brake_value)
            elif control == AvailableControls.Clutch:
                if self.stop_clutch_thread:
                    self.stop_clutch_thread = False
                    return
                self.current_clutch_value = self.current_clutch_value + (val_diff / n_steps)
                self.clutch_pub.publish(self.current_clutch_value)
            else:
                raise Exception("Control not available." + str(control))
            
            sleep(update_time / n_steps)
