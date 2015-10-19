#!/usr/bin/env python  
import rospy
import math
import tf
from sensor_msgs.msg import JointState
import geometry_msgs.msg
import visualization_msgs.msg 

if __name__ == '__main__':
    rospy.init_node('planar_robot')

    listener = tf.TransformListener()



    end_eff = rospy.Publisher('marker', visualization_msgs.msg.Marker, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('base_link', 'link3', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        xtrans = trans[0]
        ytrans = trans[1]

        vm = visualization_msgs.msg.Marker()
        vm.xtrans.x = xtrans
        vm.ytrans.y = ytrans
        end_eff.publish(vm)

        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.header.stamp = rospy.Time(0);
        marker.ns = "marker_uno";
        marker.id = 0;
        marker.type = 4
        marker.pose.position.x = xtrans
        marker.pose.position.y = ytrans
        marker.pose.position.z = 0
        marker.point.position.x = xtrans
        marker.point.position.y = ytrans
        marker.point.position.z = 0.0
        marker.color.a = 1.0 #Don't forget to set the alpha!
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0

        rate.sleep()