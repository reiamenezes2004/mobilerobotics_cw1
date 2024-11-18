#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def init_publisher():
    rospy.init_node('turtlesim_navigation', anonymous=True)  # Initialize the ROS node
    cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  # Setup publisher
    rospy.loginfo("Publisher initialized. Node is running.")
    return cmd_vel_pub

if __name__ == '__main__':
    try:
        cmd_vel_pub = init_publisher()
    except rospy.ROSInterruptException:
        pass
