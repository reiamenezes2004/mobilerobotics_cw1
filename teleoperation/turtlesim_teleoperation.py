#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

# initialize variables
speed = 1.0         # declaring linear speed (m/s)
turn_speed = 1.0    # declaring angular (rotation) speed (rad/s)
update_speed = False  # flag to indicate speed update
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
    global speed, turn_speed, update_speed
    try:
        if key.char in move_bindings:
            # sets the movement based on the key pressed
            linear, angular = move_bindings[key.char]
            twist.linear.x = linear * speed
            twist.angular.z = angular * turn_speed
            pub.publish(twist)
        elif key.char == 's':  # flag for speed update
            update_speed = True
    except AttributeError:
        pass

def on_release(key):
    global update_speed
    # stop the turtle once the key pressed is released
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)
    # exits program on esc 'escape'
    if key == keyboard.Key.esc:
        return False
    
# function to handle user input for speed
# def get_new_speed():
#     global speed, turn_speed, update_speed
#     try:
        # Prompt for new linear speed
        new_speed_input = input("Enter new linear speed (m/s): ").strip()
        # Validate and convert the input
        new_speed = float(new_speed_input) if new_speed_input else speed  # Use existing speed if no input
        # Prompt for new angular speed
        new_turn_speed_input = input("Enter new angular speed (rad/s): ").strip()
        # Validate and convert the input
        new_turn_speed = float(new_turn_speed_input) if new_turn_speed_input else turn_speed  # Use existing turn speed if no input
        # Update global speed variables
        speed = new_speed
    #     turn_speed = new_turn_speed
    #     print(f"Updated speed: Linear = {speed} m/s, Angular = {turn_speed} rad/s")
    # except ValueError:
    #     print("Invalid input. Please enter valid numeric values.")
    # finally:
    #     update_speed = False  # reset the flag


# main function to run the turtle teleoperation
def teleop_turtle_with_hold():
    global update_speed
    print("Control Your Turtle! Press 'f', 'b', 'l', 'r' to move and release to stop.")
    print("Press 's' to input new speed values for linear and angular speed.")
    print("Press 'esc' to exit.")

    # # keyboard listener
    # with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    #     while listener.running:
    #         # if update_speed:  # check if the speed update flag is set
    #         #     # get_new_speed()
    #         # rate.sleep()

# run the teleoperation function
if __name__ == '__main__':
    try:
        teleop_turtle_with_hold()
    except rospy.ROSInterruptException:
        pass
