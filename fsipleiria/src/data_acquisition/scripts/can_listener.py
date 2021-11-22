import rospy
from can_msgs.msg import Frame
import json
import redis

class Message:
    
    id = None
    is_rtr = None
    is_extended = None
    is_error = None
    dlc = None
    data = None

def callback(data):
    
    rospy.loginfo(rospy.get_caller_id() + " - received %d", data.id)

    # write this data to cache
    f = Message()
    f.id = data.id
    f.is_rtr = data.is_rtr
    f.is_extended = data.is_extended
    f.is_error = data.is_error
    f.dlc = data.dlc
    f.data = list(data.data)

    print(json.dumps(f.__dict__))

    r = redis.Redis(host='localhost', port=6379, db=0)

    r.hset('can_messages', f.id, json.dumps(f.__dict__))

    r.close()


def publisher():

    rospy.init_node('can_listener', anonymous=True)

    rospy.Subscriber("/received_messages", Frame, callback)

    rospy.spin()

if __name__ == '__main__':
    publisher()