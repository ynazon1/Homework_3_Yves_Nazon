#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
        
def planar_robot():
    rospy.init_node('planar_robot', anonymous=True)
    pub = rospy.Publisher('joint_states', JointState, queue_size=1)
    
    
    l1 = 1
    l2 = 1
    t0 = rospy.get_time() 
    js = JointState()
    
    while not rospy.is_shutdown():

        t1 = rospy.get_time()
        t2 = rospy.Time.now()
        t3 = t2.to_sec()
        
        #t_ime = t3
        t = t3
        
        xpos = 0.5*math.cos((2*math.pi*t)/5.0) + 1.25
        ypos = 0.5*math.sin((2*math.pi*t)/5.0)

        

        print t
        #xpos = int(xpos)
        #ypos = int(ypos)

        #a = l1
        #b = l2
        # = xpos
        #h = ypos
        #f = (d**2 + h**2 - a**2 - b**2)/(2*a)

        #theta2 = 2*math.atan2(1*math.sqrt(b**2 - f**2),b + f)

        #m = a + b*math.cos(theta2)
        #n = b + math.sin(theta2)

        #x1 = (d*m + h*n)/(m**2 + n**2)
        #y1 = (h - n*x1)/m

        #theta1 = math.atan2(y1,x1)

        #theta21 = 2*math.atan2(math.sqrt(part1/part2))
        
        theta2 = math.acos(((xpos**2)+(ypos**2)-(l1**2)-(l2**2))/(2*l1*l2))
        phi = math.atan2(ypos,xpos)
        psi = math.atan2(l2*math.sin(theta2),(l1+l2*math.cos(theta2)))
        theta1 = phi - psi

        theta_input= [theta1,theta2]
        header= t2
        name=['joint1','joint2']

        js.header.stamp = header
        js.position = theta_input
        js.name = name

        
        rate = rospy.Rate(40) # 50hz

        rospy.loginfo(js)
        pub.publish(js)
        rate.sleep()


if __name__ == '__main__':
    try:
        planar_robot()
    except rospy.ROSInterruptException:
        pass