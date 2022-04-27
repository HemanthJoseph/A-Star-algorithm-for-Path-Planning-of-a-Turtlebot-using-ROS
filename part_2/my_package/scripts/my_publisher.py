#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('Action_Set_Velocity_Publisher')
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
rate = rospy.Rate(1)
move = Twist()
move.linear.x = 1
move.angular.y = 1

while not rospy.is_shutdown():
	pub.publish(move)
	rate.sleep()
