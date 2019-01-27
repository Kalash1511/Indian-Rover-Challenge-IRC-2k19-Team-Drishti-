#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
import serial
import MySQLdb as mdb
import time
import subprocess

def keys_cb(msg,sensor_pub):
        if (msg.buttons[0]==1) :
                ser=serial.Serial('/dev/ttyACM0',9600)
                while (msg.buttons[1]!=1):
                        data=ser.readline()
                        time.sleep(1)
                        data=ser.readline()
                        print data
                        pieces=data.split("\t")

                        soil_moisture=pieces[0]
                        gas=pieces[1]
                        temp=pieces[2]
                        pres=pieces[3]

                        con=mdb.connect('localhost','root','1234','Sensor');
                        with con:
                                cursor=con.cursor()
                                cursor.execute("""TRUNCATE TABLE test""")
                                cursor.execute("""INSERT INTO  test VALUES(NULL,%s,%s,%s,%s)""",(soil_moisture,temp,gas,pres))	
                                con.commit()
                                cursor.close()
                if(msg.buttons[2]==1):
                        subprocess.call('python3','stitch.py')
if __name__ =='__main__':
        rospy.init_node('JOYSTICK SENSOR')
        sensor_pub = rospy.Publisher('sensor',queue_size = 50)
        rospy.Subscriber('joy',Joy,keys_cb,sensor_pub)
