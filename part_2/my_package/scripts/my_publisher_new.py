#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('Action_Set_Velocity_Publisher')
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(1)
move = Twist()

###

radius = 0.033 #radius of turtlebot3 burger wheel
Length = 0.16 #crosssectional length of turtlebot3 burger

actions_Set = [[50,50],[50,0],[50,50],[0,50],[50,50],[50,100],[100,100],[100,50],[100,100],[0,100],[100,100],[100,0]]
while not rospy.is_shutdown():
	while True:
		if len(actions_Set) == 0:
			move.linear.x = 0
			move.angular.z = 0
			pub.publish(move)
			break
		RPM = actions_Set.pop()
		left_vel_ang = (RPM[0]/60) * 2 * (22/7)
		left_vel_linear = left_vel_ang * radius
		
		right_vel_ang = (RPM[1]/60) * 2 * (22/7)
		right_vel_linear = right_vel_ang * radius
		
		average_linear_velocity = (left_vel_linear + right_vel_linear)/2
		angle_z = (right_vel_linear - left_vel_linear)/Length
		
		#go straight
		if RPM[0] == RPM[1]:
			move.linear.x = average_linear_velocity
			move.angular.z = 0
		else: #take turn
			move.linear.x = average_linear_velocity
			move.angular.z = angle_z
		pub.publish(move)
		rate.sleep()

