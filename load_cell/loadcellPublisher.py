#!/usr/bin/env python

import rospy 
import serial

from std_msgs.msg import Float32 

ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

def talker():
  pub = rospy.Publisher("loadcell", Float32, queue_size=10) 
  rospy.init_node("loadcellPublisher", anonymous=True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    ser_bytes = ser.readline() 
    weight = ser_bytes.decode() 
    rospy.loginfo("Weight: " + weight + "g") 
    pub.publish(weight) 
    rate.sleep() 

if __name__ == '__main__':
  try:
    talker() 
  except rospy.ROSInterruptException:
    pass

