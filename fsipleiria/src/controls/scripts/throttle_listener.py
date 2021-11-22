import rospy
from std_msgs.msg import Float64
from can_msgs.msg import Frame
import redis
import json

def callback(data):

    throttle_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", throttle_value)

    # get last frame received with this id
    r = redis.Redis(host='localhost', port=6379, db=0)

    frame = r.hget("can_messages", str(0x6A))

    if frame is None:
        raise Exception("A frame of this type was not received yet.")
    
    frame = json.loads(frame)

    r.close()

    # write the value to the bytes and send to the bus

    frame["data"][2] = (throttle_value & 0xFF00) >> 8
    frame["data"][3] = throttle_value & 0xFF

    f = Frame()

    f.id = frame["id"]
    f.dlc = frame["dlc"]
    f.data = frame["data"]
    f.is_error = False
    f.is_rtr = False

    can_publisher.publish(f)


def listener():

    rospy.init_node('throttle_listener', anonymous=True)

    global can_publisher
    can_publisher = rospy.Publisher("sent_messages", Frame, queue_size=10);

    rospy.Subscriber("controls/throttle", Float64, callback)    

    rospy.spin()

if __name__ == '__main__':
    listener()