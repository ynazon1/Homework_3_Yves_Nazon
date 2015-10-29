#!/usr/bin/env python  
import rospy
import math
import tf
import visualization_msgs.msg
import geometry_msgs.msg

if __name__ == '__main__':
    rospy.init_node('planar_robot_listener')

    listener = tf.TransformListener()

    end_eff = rospy.Publisher('marker', visualization_msgs.msg.Marker, queue_size=1)
    rate = rospy.Rate(10.0)

    vm = visualization_msgs.msg.Marker()
    marker = vm
    marker.header.frame_id = "base_link"
    marker.ns = "marker_uno";
    marker.id = 0;
    marker.type = 4
    point_list = []
    marker.color.a = 1.0 #Don't forget to set the alpha!
    marker.color.r = 0.0
    marker.color.g = 1.0
    marker.color.b = 0.0
    marker.scale = geometry_msgs.msg.Vector3(0.01, 0.01, 0.01)
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('base_link', 'link3', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        xtrans = trans[0]
        ytrans = trans[1]

        gm = geometry_msgs.msg.Point(xtrans, ytrans, 0)
        if len(point_list) > 30:
            point_list.pop(0)
        point_list.append(gm)
        vm.points = point_list
        vm.header.stamp = rospy.Time.now()
        end_eff.publish(vm)

        rate.sleep()
