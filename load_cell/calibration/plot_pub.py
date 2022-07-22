#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32
from dotenv import load_dotenv

load_dotenv()
DATA_FILE_PATH = r'%s' % os.getenv('PATH_TO_DATA_FILE')

previousLineCount = 0 

def talker(previousLineCount):
  pub = rospy.Publisher('voltageRatioPlot', Float32, queue_size=50)
  rospy.init_node('plot_pub', anonymous=True)
  rate = rospy.Rate(10) 
  while not rospy.is_shutdown():
    with open(DATA_FILE_PATH, 'r') as fp:
      lines = fp.readlines()
      lineCount = len(lines)
      if (lineCount>previousLineCount):
        previousLineCount = lineCount 
        latestReading = float(lines[-1]) 
        rospy.loginfo(lines[-1]) 
        # calibrated  
        f = (latestReading * 1.01297885e+06 + 9.77941741e+01) * 9.81 / 1000
        pub.publish(f) 
        
        rate.sleep() 

if __name__ == '__main__':
  try:
    talker(previousLineCount) 
  except rospy.ROSInterruptException:
    pass
        




