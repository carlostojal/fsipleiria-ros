import rospy
from can_msgs.msg import Frame
from data_acquisition.msg import Geolocation
from time import sleep

def callback(data):
    
    rospy.loginfo(rospy.get_caller_id() + " - received %d", data.id)

    # frame id is 0x6E
    # GPS longitude is on bytes B7 and B6 (or B5 and B4)
    # GPS latitude is on bytes B3 and B2 (or B1 and B0)

    if data.id == 0x6E:
        longitude = (data.data[0] << 8) | data.data[1]
        latitude = (data.data[4] << 8) | data.data[5]

        rospy.loginfo("Longitude: %f", longitude)
        rospy.loginfo("Latitude: %f", latitude)

        msg = Geolocation()

        msg.header.stamp = rospy.Time.now()
        msg.longitude = longitude
        msg.latitude = latitude

        print(str(msg))

        publisher.publish(msg)


def publisher():

    rospy.init_node('geolocation_publisher', anonymous=True)

    rospy.Subscriber("/received_messages", Frame, callback)

    global publisher
    publisher = rospy.Publisher('/data_acquisition/geolocation', Geolocation, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    publisher()