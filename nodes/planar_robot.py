#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from sensor_msgs.msg import JointState

def planar_robot():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('planar_robot', anonymous=True)
    rate = rospy.Rate(50) # 50hz
    use_gui:=true
    while not rospy.is_shutdown():
        js = 
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        planar_robot()
    except rospy.ROSInterruptException:
        pass