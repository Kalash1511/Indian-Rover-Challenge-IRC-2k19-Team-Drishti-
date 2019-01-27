#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from pcl_msgs.msg import Vertices
import serial


class driver:
    def __init__(self):
        # init ros
        rospy.init_node('manuplator_driver', anonymous=True)
        rospy.Subscriber('manuplator_length', Vertices, self.get_cmd_vel)
        self.ser = serial.Serial('/dev/ttyACM0',9600)
        self.get_arduino_message()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self,data):
        a1 = data.vertices[0]
        a2 = data.vertices[1]
        a3 = data.vertices[2]

        m1 = data.vertices[3]
        m2 = data.vertices[4]
        m3 = data.vertices[5]
	   m4 = data.vertices[6]
	   m5 = data.vertices[7]

        d  = data.vertices[8]

        self.send_cmd_to_arduino(a1,a2,a3,m1,m2,m3,m4,m5,d)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self,a1,a2,a3,m1,m2,m3,m4,m5,d):
        # calculate actuator 1 feed back resistor signal
    	acutator1=a1
    	acutator2=a2
    	acutator3=a3

    	motor1=m1
    	motor2=m2
    	motor3=m3
    	motor4=m4
    	motor5=m5



        default=d 
        # format for arduino
        message = "{},{},{},{},{},{},{},{},{}*".format(acutator1,acutator2,acutator3,motor1,motor2,motor3,motor4,motor5,default) 
    	print message
        self.ser.write(message)

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('manuplator_arduino', String, queue_size=50)
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            message = self.ser.readline()
            pub.publish(message)
            r.sleep()

if __name__ == '__main__':
    try:
        d = driver()
    except rospy.ROSInterruptException: 
        pass


