#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Joy
from pcl_msgs.msg import Vertices

#import array as m



def joystick_cb(msg, manuplator_pub):

	#stop code
	if msg.buttons[8]==1:
		m=[0,0,0,0,0,0,0,0,0]
		manuplator_pub.publish(m)

	#reseting code
	#stop code
	if msg.buttons[9]==1:
		m=[0,0,0,0,0,0,0,0,10]
		manuplator_pub.publish(m)
	
	
	#linear actuator 1
	if msg.buttons[0]==1 and msg.axes[5]==1:#linear_actuator_1
		m=[1,0,0,0,0,0,0,0,0]
		manuplator_pub.publish(m)

	if msg.buttons[0]==1 and msg.axes[5]==-1:#linear_actuator_1
		m=[2,0,0,0,0,0,0,0,0]
		manuplator_pub.publish(m)	

	#linear actuator 2	
	if msg.buttons[1]==1 and msg.axes[5]==1:#linear_actuator_2
		m=[0,1,0,0,0,0,0,0,0]
		manuplator_pub.publish(m)	

	if msg.buttons[1]==1 and msg.axes[5]==-1:#linear_actuator_2
		m=[0,2,0,0,0,0,0,0,0]
		manuplator_pub.publish(m)	
		
	#linear actuator 3		
	if msg.buttons[2]==1 and msg.axes[5]==1:#linear_actuator_3
		m=[0,0,1,0,0,0,0,0,0]
		manuplator_pub.publish(m)

	if msg.buttons[2]==1 and msg.axes[5]==-1:#linear_actuator_3
		m=[0,0,2,0,0,0,0,0,0]
		manuplator_pub.publish(m)	
		
	#motor 1	
	if msg.buttons[0]==1 and msg.axes[4]==1:#motor_1
		m=[0,0,0,1,0,0,0,0,0]
		manuplator_pub.publish(m)
		
	if msg.buttons[0]==1 and msg.axes[4]==-1:#motor_1
		m=[0,0,0,2,0,0,0,0,0]
		manuplator_pub.publish(m)		

	# motor 2		
	if msg.buttons[1]==1 and msg.axes[4]==1:#motor_2
		m=[0,0,0,0,1,0,0,0,0]
		manuplator_pub.publish(m)

	if msg.buttons[1]==1 and msg.axes[4]==-1:#motor_2
		m=[0,0,0,0,2,0,0,0,0]
		manuplator_pub.publish(m)
				
	# motor 3		
	if msg.buttons[2]==1 and msg.axes[4]==1:#motor_3
		m=[0,0,0,0,0,1,0,0,0]
		manuplator_pub.publish(m)

	if msg.buttons[2]==1 and msg.axes[4]==-1:#motor_3
		m=[0,0,0,0,0,2,0,0,0]				
		manuplator_pub.publish(m)

	# motor 4		
	if msg.buttons[4]==1 and msg.axes[4]==1:#motor_3
		m=[0,0,0,0,0,0,1,0,0]
		manuplator_pub.publish(m)

	if msg.buttons[4]==1 and msg.axes[4]==-1:#motor_3
		m=[0,0,0,0,0,0,2,0,0]				
		manuplator_pub.publish(m)
			
	# motor 5		
	if msg.buttons[5]==1 and msg.axes[4]==1:#motor_3
		m=[0,0,0,0,0,0,0,1,0]
		manuplator_pub.publish(m)

	if msg.buttons[5]==1 and msg.axes[4]==-1:#motor_3
		m=[0,0,0,0,0,0,0,2,0]				
		manuplator_pub.publish(m)
			
	#default position
	if msg.buttons[6]==1 and msg.axes[5]==1:#default position 1
		m=[0,0,0,0,0,0,0,0,1]				
		manuplator_pub.publish(m)

	if msg.buttons[4]==1 and msg.axes[5]==1:#default position 2
		m=[0,0,0,0,0,0,0,0,2]				
		manuplator_pub.publish(m)
	
	if msg.buttons[7]==1 and msg.axes[5]==1:#default position 3
		m=[0,0,0,0,0,0,0,0,3]				
		manuplator_pub.publish(m)

	if msg.buttons[5]==1 and msg.axes[5]==1:#default position 4
		m=[0,0,0,0,0,0,0,0,4]				
		manuplator_pub.publish(m)

	if msg.buttons[6]==1 and msg.axes[5]==-1:#default position 5
		m=[0,0,0,0,0,0,0,0,5]				
		manuplator_pub.publish(m)

	if msg.buttons[4]==1 and msg.axes[5]==-1:#default position 6
		m=[0,0,0,0,0,0,0,0,6]				
		manuplator_pub.publish(m)
	
	if msg.buttons[7]==1 and msg.axes[5]==-1:#default position 7
		m=[0,0,0,0,0,0,0,0,7]				
		manuplator_pub.publish(m)

	if msg.buttons[5]==1 and msg.axes[5]==-1:#default position 8
		m=[0,0,0,0,0,0,0,0,8]				
		manuplator_pub.publish(m)	
	

if __name__ == '__main__':
	rospy.init_node('JOYstick')
	manuplator_pub = rospy.Publisher('manuplator_length',Vertices,queue_size=50)
	rospy.Subscriber('joy',Joy,joystick_cb, manuplator_pub)
	rospy.spin()
