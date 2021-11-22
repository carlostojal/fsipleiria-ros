import rospy
from can_msgs.msg import Frame
from std_msgs.msg import Float64

def callback(data):
    
    rospy.loginfo(rospy.get_caller_id() + " - received %d", data.id)

    # frame id is 0x60
    # Engine Speed is on bytes B1 and B0

    if data.id == 0x60:

        engine_speed = (data.data[6] << 8) | data.data[7]

        rospy.loginfo("Engine speed: %f", engine_speed)

        msg = engine_speed

        print(str(msg))

        publisher.publish(msg)


def publisher():

    rospy.init_node('engine_speed_publisher', anonymous=True)

    rospy.Subscriber("/received_messages", Frame, callback)

    global publisher
    publisher = rospy.Publisher('/data_acquisition/engine_speed', Float64, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    publisher()