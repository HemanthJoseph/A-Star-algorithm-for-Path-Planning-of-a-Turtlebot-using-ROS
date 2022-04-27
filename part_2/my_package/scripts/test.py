radius = 0.033 #radius of turtlebot3 burger wheel

actions_Set = [[50,50],[50,0],[0,50],[50,100],[100,50],[100,100],[0,100],[100,0]]
for each in actions_Set:
	if each[0] == each[1]:
		wheel_ang_vel = (each[0]/60) * 2 * 3.14
		wheel_linear_vel_x = wheel_ang_vel * radius
		wheel_ang_z = 0
	elif each[0] > each[1]:
		wheel_linear_vel_x = 0
		wheel_ang_z = 1
	elif each[0] < each[1]:
		wheel_linear_vel_x = 0
		wheel_ang_z = -1
	print(wheel_linear_vel_x)
	print(wheel_ang_z)
