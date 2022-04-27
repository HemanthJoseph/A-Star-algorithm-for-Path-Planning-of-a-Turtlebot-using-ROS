* Implementation of A Start algorithm - Project 3 Phase 2 - part 2 (ROS implementation and Gazebo visualization)
By - Hemanth Joseph Raj (117518955) and Venkata Sri Ranga Sai Anapu (118529950) 


* Files in the directory:
     1) The ROS package - my_package
     2) Video
     3) This readme file

####### Instructions to run the code #######
* Navigate inside the part 2 folder
* Copy the my_package folder into your catkin workspace
* First we need to compile our ROS package
  - Open your terminal and navigate to your catkin workspace
  - run the following code <catkin_make>
  - In case you have used catkin build before run <catkin clean> and then run <catkin build>
* Once we have run "catkin_make", we need to source our environment
  - In the same terminal run <source devel/setup.bash>
* After sourcing, we need to run our ros file
  - In the same terminal run <roslaunch my_package world_launch.launch>
  - This will launch the Gazebo which will spawn our Turtlebot3 burger model in the provided world
* Now we need to run our publisher
  - Open a new terminal window or tab
  - Source the termianl by running <source devel/setup.bash>
  - Once it is sourced, run <rosrun my_package my_publisher_new.py>
  - This will start the publisher node which keeps publishing linear velocity and angular velocity values to 'cmd_vel' topic
* The Turtlebot3 which inherently subscribes to 'cmd_vel', receives the commands and moves accordingly
* Once code is run press 'CTRL + C' in each terminal and terminate the programs

## NOTE!!! ###
> We weren't able to convert our path received from part 1 into respective wheel RPMs (left and right) needed for the ROS Publisher program.
> So I gave a sample action set to the publisher program to move around in the Gazebo
> This was done so as to prove that our publisher program is working properly
