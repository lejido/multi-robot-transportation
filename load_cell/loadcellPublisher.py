#!/usr/bin/env python

import rospy 
import serial

from std_msgs.msg import String

prt = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AB0JPNGI-if00-port0"

ser = serial.Serial(prt)
# ser.timeout = 1.0
ser.flushInput() #get rid of unwanted input stuff  

def talker():
  pub = rospy.Publisher("loadcell", String, queue_size=10) 
  rospy.init_node("loadcellPublisher", anonymous=True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    ser_bytes = ser.readline() 
    weight = (ser_bytes.decode()).strip() 
    rospy.loginfo("Weight: " + weight + "g") 
    pub.publish(weight) 
    rate.sleep() 

if __name__ == '__main__':
  try:
    talker() 
  except rospy.ROSInterruptException:
    pass

