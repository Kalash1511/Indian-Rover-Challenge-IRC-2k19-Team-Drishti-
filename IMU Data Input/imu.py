#!/usr/bin/env python
import rospy
import sys
sys.path.append('.')
import RTIMU
import os.path
import time
import math
from sensor_msgs.msg import Imu
SETTINGS_FILE = "RTIMULib"
s = RTIMU.Settings(SETTINGS_FILE)
def imu_talker():
    # setup publisher and classes
    pub = rospy.Publisher('imu', Imu, queue_size=10)
    rospy.init_node('imu_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    imu = RTIMU.RTIMU(s)
    if (not imu.IMUInit()):
        sys.exit(1)
    # set parameters
    imu.setSlerpPower(0.02)
    imu.setGyroEnable(True)
    imu.setAccelEnable(True)
    imu.setCompassEnable(True)
    seq = 0
    while not rospy.is_shutdown():
        if imu.IMURead():
            data = imu.getIMUData()
            seq += 1
            msg.header.seq = seq
            msg.header.stamp = rospy.Time.now()
            if data['compassValid'] == True:
                msg.orientation.x = data['compass'][0]
                msg.orientation.y = data['compass'][1]
                msg.orientation.z = data['compass'][2]
                msg.orientation.w = 0
                msg.angular_velocity.x = data['accel'][0]
                msg.angular_velocity.y = data['accel'][1]
                msg.angular_velocity.z = data['accel'][2]
            if data['gyroValid'] == True:
                msg.linear_acceleration.x = data['gyro'][0]
                msg.linear_acceleration.y = data['gyro'][1]
                msg.linear_acceleration.z = data['gyro'][2]
        pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        imu_talker()
    except rospy.ROSInterruptException:
        pass