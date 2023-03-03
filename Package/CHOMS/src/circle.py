#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64


def teleop():
    rospy.init_node('teleop')

    pub_right = rospy.Publisher('/CHOMS/right_steering_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/CHOMS/left_steering_controller/command', Float64, queue_size=10)
    pub_rear_right = rospy.Publisher('/CHOMS/rear_right_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    pub_rear_left = rospy.Publisher('/CHOMS/rear_left_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(10)

    control_turn = 1
    control_speed = 10

    while not rospy.is_shutdown():
        pub_right.publish(-control_turn) # publish the turn command.
        pub_left.publish(-control_turn) # publish the turn command.
        pub_rear_right.publish(-control_speed) # publish the control speed. 
        pub_rear_left.publish(-control_speed)
        rospy.loginfo("right_turn: %s",control_turn)
        rospy.loginfo("left_turn: %s",control_turn)
        rospy.loginfo("speed: %s",control_speed)
        
        rate.sleep()

if __name__=="__main__":
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass