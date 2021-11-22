import rospy
from can_msgs.msg import Frame
from std_msgs.msg import Float64
import redis
import json

def callback(data):

    steering_value = data.data

    rospy.loginfo(rospy.get_caller_id() + " - received %f", steering_value)

    # get last frame received with this id
    r = redis.Redis(host='localhost', port=6379, db=0)

    frame = r.hget("can_messages", str(0x6D))

    if frame is None:
        raise Exception("A frame of this type was not received yet.")

    frame = json.loads(frame)

    r.close()

    # write the value to the bytes and send to the bus

    frame["data"][4] = (steering_value & 0xFF00) >> 8
    frame["data"][5] = steering_value & 0xFF

    f = Frame()

    f.id = frame["id"]
    f.dlc = frame["dlc"]
    f.data = frame["data"]
    f.is_error = False
    f.is_rtr = False

    can_publisher.publish(f)


def listener():

    rospy.init_node('steering_listener', anonymous=True)

    global can_publisher
    can_publisher = rospy.Publisher("sent_messages", Frame, queue_size=10)

    rospy.Subscriber("controls/steering", Float64, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()