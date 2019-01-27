#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

t = Twist()

def keys_cb(msg, twist_pub):
	
	base=10

	#forward movement
	if msg.buttons[0]==1 and msg.axes[5]==1:
		t.linear.x=base*0.30
		t.angular.z=base*0.0
	if msg.buttons[1]==1 and msg.axes[5]==1:
		t.linear.x=base*0.7
		t.angular.z=base*0.0
	if msg.buttons[2]==1 and msg.axes[5]==1:
		t.linear.x=base*0.80
		t.angular.z=base*0.0
	if msg.buttons[3]==1 and msg.axes[5]==1:
		t.linear.x=base*0.9
		t.angular.z=base*0.0
	if msg.buttons[7]==1 and msg.axes[5]==1:
		t.linear.x=base*1.0
		t.angular.z=base*0.0
	
	#backward movement
	if msg.buttons[0]==1 and msg.axes[5]==-1:
		t.linear.x=-(base*0.30)
		t.angular.z=base*0.0

	if msg.buttons[1]==1 and msg.axes[5]==-1:
		t.linear.x=-(base*0.7)
		t.angular.z=base*0.0
			
	if msg.buttons[2]==1 and msg.axes[5]==-1:
		t.linear.x=-(base*0.80)
		t.angular.z=base*0.0
		
	if msg.buttons[3]==1 and msg.axes[5]==-1:
		t.linear.x=-(base*0.9)
		t.angular.z=base*0.0
		
	if msg.buttons[7]==1 and msg.axes[5]==-1:
		t.linear.x=-(base*1.0)
		t.angular.z=base*0.0
	


	#movement left
	if msg.buttons[0]==1 and msg.axes[4]==1:
		t.angular.z=(base*0.20)
		t.linear.x=(base*0.80)
		
	if msg.buttons[1]==1 and msg.axes[4]==1:
		t.angular.z=(base*0.80)
		t.linear.x=(base*0.20)
			
	if msg.buttons[2]==1 and msg.axes[4]==1:
		t.angular.x=(base*0.20)
		t.linear.z=base*0.70
		
	if msg.buttons[3]==1 and msg.axes[4]==1:
		t.angular.z=(base*0.70)
		t.linear.x=base*0.20
		
	if msg.buttons[7]==1 and msg.axes[4]==1:
		t.angular.z=-(base*0.8)
		t.linear.x=0
	

	#movement right
	if msg.buttons[0]==1 and msg.axes[4]==-1:
		t.angular.z=-(base*0.20)
		t.linear.x=base*0.80
		
	if msg.buttons[1]==1 and msg.axes[4]==-1:
		t.angular.z=-(base*0.80)
		t.linear.x=base*0.20
		
	if msg.buttons[2]==1 and msg.axes[4]==-1:
		t.angular.z=-(base*0.20)
		t.linear.x=base*0.70
		
	if msg.buttons[3]==1 and msg.axes[4]==-1:
		t.angular.z=-(base*0.70)
		t.linear.x=base*0.20
		
	if msg.buttons[7]==1 and msg.axes[4]==-1:
		t.angular.z=base*0.8
		t.linear.x=0
	

	#stop code 
	if msg.buttons[8]==1:
		t.angular.z=0
		t.linear.x=0

	twist_pub.publish(t)

if __name__ == '__main__':
	rospy.init_node('JOYstick')
	twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=50)
	rospy.Subscriber('joy',Joy, keys_cb, twist_pub)
	rospy.spin()
