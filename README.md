# homework-2-ynazon1
<<<<<<< HEAD
=======
homework-2-ynazon1 created by Classroom for GitHub

#----Package Description----

This ROS package models a 2-DOF planar robot using an inverse kinematics method. (shown in figure![link](http://nu-msr.github.io/embedded-course-site/public/images/two-link-robot-mls.png)). This package has two primary node called `planar_robot.py` and `planar_robot_listener.py`. A model of the robot from figure 1 is created in rviz by a URDF named `planar_robot.urdf` and can be seen traversing a circular trajectory. To run the nodes of this package run the launch file `pl_bot.launch`.

#----Nodes----

planar_robot.py

This node publishes to the joint_state topic a specific trajectory for the planar robot at 50 Hz. This trajectory is described by the movement of the angles theta 1 and 2 respectively. Theta 1&2 are the position input vector to the JointState message. The name of the joints designated in the URDF and a header time stamp are also required for the JointState message to run in this node.

planar_robot_listener.py

This node publishes a`visualization_msgs/Marker` message at a rate of 10 Hz and is supposed to create a marker that follows the path of the end effector at the edge of link 2. This node subscribes to tf to find out he path taken by the end effector.

#----Launch File Information----
This launch file permits the option to use a GUI with `joint_state_publisher` and automatically starts the `planar_robot.py` and `planar_robot_listener.py` nodes along with [rviz] and `robot_state_publisher`

#----Other Notes----
* Inverse Kinematic Equations taken from Lecturer Damian Gordon (Dublin Institute of Technology) presentation 

* Some portion of code was based off work from trep_puppet_demo project




>>>>>>> 6f01e3932c77e7138be81b00b00ef3b41296174d
