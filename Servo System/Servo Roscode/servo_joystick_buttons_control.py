#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32MultiArray
import array as m

#t = Twist()

#k[] = Int32[]

def servo_cb(msg, twist_pub):


	#default position
	if(msg.buttons[9]==1)
		m.array('b',[0,0])

	# upward 0 - 90
	if (axes.buttons[5]==1 && msg.buttons[0]==1):
		m.array('b',[20,0])

	if (axes.buttons[5]==1 && msg.buttons[1]==1):
		m.array('b',[40,0])
		
	if (axes.buttons[5]==1 && msg.buttons[2]==1):
		m.array('b',[60,0])
		
	if (axes.buttons[5]==1 && msg.buttons[3]==1):
		m.array('b',[80,0])
		
	if (axes.buttons[5]==1 && msg.buttons[7]==1):
		m.array('b',[90,0])				
	
	# downward 0 - -90
	if (axes.buttons[5]==-1 && msg.buttons[0]==1):
		m.array('b',[-20,0])

	if (axes.buttons[5]==-1 && msg.buttons[1]==1):
		m.array('b',[-40,0])
		
	if (axes.buttons[5]==-1 && msg.buttons[2]==1):
		m.array('b',[-60,0])
		
	if (axes.buttons[5]==-1 && msg.buttons[3]==1):
		m.array('b',[-80,0])
		
	if (axes.buttons[5]==-1 && msg.buttons[7]==1):
		m.array('b',[-90,0])	


	# left 0 - 90
	if (axes.buttons[4]==1 && msg.buttons[0]==1):
		m.array('b',[20,0])

	if (axes.buttons[4]==1 && msg.buttons[1]==1):
		m.array('b',[40,0])
		
	if (axes.buttons[4]==1 && msg.buttons[2]==1):
		m.array('b',[60,0])
		
	if (axes.buttons[4]==1 && msg.buttons[3]==1):
		m.array('b',[80,0])
		
	if (axes.buttons[4]==1 && msg.buttons[7]==1):
		m.array('b',[90,0])				
	
	# right 0 - -90
	if (axes.buttons[4]==-1 && msg.buttons[0]==1):
		m.array('b',[-20,0])

	if (axes.buttons[4]==-1 && msg.buttons[1]==1):
		m.array('b',[-40,0])
		
	if (axes.buttons[4]==-1 && msg.buttons[2]==1):
		m.array('b',[-60,0])
		
	if (axes.buttons[4]==-1 && msg.buttons[3]==1):
		m.array('b',[-80,0])
		
	if (axes.buttons[4]==-1 && msg.buttons[7]==1):
		m.array('b',[-90,0])		
	
					

	man_pub.publish(m)

if __name__ == '__main__':
	rospy.init_node('servo_controller')
	servo_pub = rospy.Publisher('servo_vel', Int32MultiArray, queue_size=5)
	rospy.Subscriber('joy',Joy,servo_cb,servo_pub)
	rospy.spin()
