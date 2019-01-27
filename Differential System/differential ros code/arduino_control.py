
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import serial


class driver:
    def __init__(self):
        # init ros
        rospy.init_node('rover_driver', anonymous=True)
        rospy.Subscriber('cmd_vel',Twist,self.get_cmd_vel)
        self.ser = serial.Serial('/dev/ttyACM0', 19200)
        self.get_arduino_message()

    # get cmd_vel message, and get linear velocity and angular velocity
    def get_cmd_vel(self, data):
        x = data.linear.x
        angular = data.angular.z
        self.send_cmd_to_arduino(x, angular)

    # translate x, and angular velocity to PWM signal of each wheels, and send to arduino
    def send_cmd_to_arduino(self, x,angular,z):
        # calculate right and left wheels' signal
	
        right = int((x + angular) * 25)
        left = int((x - angular) * 25)
        # format for arduino
        message = "{},{},{},{}*".format(left, right,left,right)
        print message
        # send by serial 
        self.ser.write(message)

    # receive serial text from arduino and publish it to '/arduino' message
    def get_arduino_message(self):
        pub = rospy.Publisher('arduino', String, queue_size=50)
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


