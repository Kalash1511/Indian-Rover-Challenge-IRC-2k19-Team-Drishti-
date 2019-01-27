#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import serial


class driver:
    def __init__(self):
        # init ros
        rospy.init_node('car_driver', anonymous=True)
        rospy.Subscriber('servo_vel', Twist, self.get_cmd_vel)
        self.ser = serial.Serial('/dev/ttyACM0', 57600)
        self.get_arduino_message()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self, data):
        s1 = data.linear.x
        s2 = data.linear.y
        self.send_cmd_to_arduino(s1,s2)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self,s1,s2):
        # calculate right and left wheels' signal
        servo1=(int)(s1+90)
        servo2=(int)(s2+90)	 
        # format for arduino
        message = "{},{}*".format(servo1,servo2)
        print message
        # send by serial 
        self.ser.write(message)

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('arduino', String, queue_size=10)
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


