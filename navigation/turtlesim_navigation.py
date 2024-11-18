#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

#turtlesim_navigation

# initialising global variables
current_pose = None

# callback function to update the turtle's current position
def pose_callback(data):
    global current_pose
    current_pose = data
