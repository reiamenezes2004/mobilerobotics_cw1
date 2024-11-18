#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

# initialize variables
speed = 1.0         # declaring linear speed (m/s)
turn_speed = 1.0    # declaring angular (rotation) speed (rad/s)
move_bindings = {
    'f': (1, 0),  # moves the turtle forward
    'b': (-1, 0), # moves the turtle backward
    'l': (0, 1),  # rotates the turtle to the left
    'r': (0, -1), # rotates the turtle to the right
}

# initializing the node and publisher
rospy.init_node('turtlesim_teleoperation', anonymous=True)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

# creating a twist message
twist = Twist()

# defining the key presses and release functions
def on_press(key):
    global speed, turn_speed
    try:
        if key.char in move_bindings:
            # sets the movement based on the key pressed
            linear, angular = move_bindings[key.char]
            twist.linear.x = linear * speed
            twist.angular.z = angular * turn_speed
            pub.publish(twist)
        elif key.char == 's':  # asks the user for a new speed input
            try:
                # user inputted new linear speed
                new_speed = float(input("Enter new linear speed (m/s): "))
                # user inputted new angular speed
                new_turn_speed = float(input("Enter new angular speed (rad/s): "))
                # speed changes to updated variables
                speed = new_speed
                turn_speed = new_turn_speed
                print(f"Updated speed: Linear = {speed} m/s, Angular = {turn_speed} rad/s")
            except ValueError:
                print("Invalid input. Please enter numebers only.")
    except AttributeError:
        pass

def on_release(key):
    # stop the turtle once the key pressed is released
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)
    # exits program on esc 'escape'
    if key == keyboard.Key.esc:
        return False




