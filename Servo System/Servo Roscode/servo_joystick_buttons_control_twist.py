#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Twist

t = Twist()


def servo_cb(msg, twist_pub):


	#default position
	if(msg.buttons[9]==1)
		t.linear.x=0
		t.linear.y=0

	# upward 0 - 90
	if (axes.buttons[5]==1 && msg.buttons[0]==1):
		t.linear.x=20
		t.linear.y=0

	if (axes.buttons[5]==1 && msg.buttons[1]==1):
		t.linear.x=40
		t.linear.y=0
		
	if (axes.buttons[5]==1 && msg.buttons[2]==1):
		t.linear.x=60
		t.linear.y=0
		
	if (axes.buttons[5]==1 && msg.buttons[3]==1):
		t.linear.x=80
		t.linear.y=0
		
	if (axes.buttons[5]==1 && msg.buttons[7]==1):
		t.linear.x=90
		t.linear.y=0			
	
	# downward 0 - -90
	if (axes.buttons[5]==-1 && msg.buttons[0]==1):
		t.linear.x=-20
		t.linear.y=0

	if (axes.buttons[5]==-1 && msg.buttons[1]==1):
		t.linear.x=-40
		t.linear.y=0
		
	if (axes.buttons[5]==-1 && msg.buttons[2]==1):
		t.linear.x=-60
		t.linear.y=0
		
	if (axes.buttons[5]==-1 && msg.buttons[3]==1):
		t.linear.x=-80
		t.linear.y=0
		
	if (axes.buttons[5]==-1 && msg.buttons[7]==1):
		t.linear.x=-90
		t.linear.y=0	


	# left 0 - 90
	if (axes.buttons[4]==1 && msg.buttons[0]==1):
		t.linear.x=0
		t.linear.y=20

	if (axes.buttons[4]==1 && msg.buttons[1]==1):
		t.linear.x=0
		t.linear.y=40
		
	if (axes.buttons[4]==1 && msg.buttons[2]==1):
		t.linear.x=0
		t.linear.y=60
		
	if (axes.buttons[4]==1 && msg.buttons[3]==1):
		t.linear.x=0
		t.linear.y=80
		
	if (axes.buttons[4]==1 && msg.buttons[7]==1):
		t.linear.x=0
		t.linear.y=90				
	
	# right 0 - -90
	if (axes.buttons[4]==-1 && msg.buttons[0]==1):
		t.linear.x=0
		t.linear.y=-20

	if (axes.buttons[4]==-1 && msg.buttons[1]==1):
		t.linear.x=0
		t.linear.y=-40
		
	if (axes.buttons[4]==-1 && msg.buttons[2]==1):
		t.linear.x=0
		t.linear.y=-60
		
	if (axes.buttons[4]==-1 && msg.buttons[3]==1):
		t.linear.x=0
		t.linear.y=-80
		
	if (axes.buttons[4]==-1 && msg.buttons[7]==1):
		t.linear.x=0
		t.linear.y=-90		
	
					

	servo_pub.publish(t)

if __name__ == '__main__':
	rospy.init_node('servo_controller')
	servo_pub = rospy.Publisher('servo_vel', Twist, queue_size=5)
	rospy.Subscriber('joy',Joy,servo_cb,servo_pub)
	rospy.spin()
