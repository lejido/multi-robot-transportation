# run once for F0 and F1 for calibration
import keyboard 
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import rospy 
from std_msgs.msg import String # this probably nears to be an int msg 

import time 

def onVoltageRatioChange(self, voltageRatio):
  print("VoltageRatio: " + str(voltageRatio))
  talker(voltageRatio) 

def talker(data):
  pub = rospy.Publisher('topic_voltageRatio', String, queue_size=10) # replace string with int msg 
  rospy.init_node('talker', anonymous=True) 
  rate = rospy.Rate(10) 
  while not rospy.is_shutdown():
    voltageRatio = data  
    rospy.loginfo(data + " " + str(rospy.get_time())) 
    pub.publish(voltageRatio) 
    rate.sleep() 

def main():
  time = 30 
  timeout_start = time.time() 

  while time.time() < timeout_start + timeout:
  if (keyboard.is_pressed('q')):    
    voltageRatioInput0 = VoltageRatioInput()
    voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
    voltageRatioInput0.openWaitForAttachment(1000)
  elif (keyboard.is_pressed('p')): 
    voltageRatioInput0.close() 

main() 



















 
