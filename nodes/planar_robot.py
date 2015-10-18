#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
        
def planar_robot():
    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    rospy.init_node('planar_robot', anonymous=True)
    rate = rospy.Rate(50) # 50hz
    l1 = 1
    l2 = 1
    t0 = rospy.get_time() 
    js = JointState()
    
    while not rospy.is_shutdown():

        t1 = rospy.get_time()
        t2 = rospy.Time.now()
        t3 = t0 - t1
        t= float(t3)
        xpos = 0.5*math.cos((2*math.pi*t)/5.0)+1.25
        ypos = 0.5*math.sin((2*math.pi*t)/5.0)

        
        xpos = int(xpos)
        ypos = int(ypos)
        
        theta2 = math.acos(((xpos^2)+(ypos^2)-(l1^2)-(l2^2))/(2*l1*l2))
        phi = math.atan2(ypos,xpos)
        psi = math.atan2(l2*math.sin(theta2),l1+l2*math.cos(theta2))
        theta1 = phi - psi

        print t 
        print xpos
        print ypos

        theta_input= [theta1,theta2]
        header= t2
        name=['joint1','joint2']

        js.header.stamp = header
        js.position = theta_input
        js.name = name


        

         
        
        rospy.loginfo(js)
        pub.publish(js)
        rate.sleep()


if __name__ == '__main__':
    try:
        planar_robot()
    except rospy.ROSInterruptException:
        pass