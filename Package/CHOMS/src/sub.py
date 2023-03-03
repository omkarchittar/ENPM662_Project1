#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def callback_left(data):
    rospy.loginfo("Current left steering: %s", abs(data.data))

def callback_right(data):
    rospy.loginfo("Current right steering: %s", abs(data.data))
    
def callback_rear(data):
    rospy.loginfo("Current rear speed: %s", abs(data.data))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/CHOMS/left_steering_controller/command", Float64, callback_left)
    rospy.Subscriber("/CHOMS/right_steering_controller/command", Float64, callback_right)
    rospy.Subscriber("/CHOMS/rear_left_controller/command", Float64, callback_rear)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()