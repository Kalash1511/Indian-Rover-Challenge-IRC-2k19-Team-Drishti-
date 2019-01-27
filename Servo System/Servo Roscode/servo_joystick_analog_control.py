#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from pcl_msgs.msg import Vertices

import s as array 

def keys_cb(msg, servo_pub):
	
	speed_s1 =(int)(90+msg.axes[1]*90)
	speed_s2 =(int)(90+msg.axes[2]*90)

	s.array('b',[speed_s1,speed_s2])

	twist_pub.publish(s)

if __name__ == '__main__':
	rospy.init_node('JOYstick')
	servo_pub = rospy.Publisher('servo_vel', Vertices, queue_size=10)
	rospy.Subscriber('joy',Joy, keys_cb, servo_pub)
	rospy.spin()
