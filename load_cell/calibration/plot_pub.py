# should be in catkin workspace
# change data file path accordingly

#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32

previousLineCount = 0 

def talker(previousLineCount):
  pub = rospy.Publisher('voltageRatioPlot', Float32, queue_size=50)
  rospy.init_node('plot_pub', anonymous=True)
  rate = rospy.Rate(10) 
  while not rospy.is_shutdown():
    with open(r"/home/yoda/arpl/multi-robot-transportation/load_cell/calibration/data.txt", 'r') as fp:
      lines = fp.readlines()
      lineCount = len(lines)
      if (lineCount>previousLineCount):
        previousLineCount = lineCount 
        latestReading = float(lines[-1]) 
        rospy.loginfo(lines[-1]) 
        pub.publish(latestReading) 
        rate.sleep() 

if __name__ == '__main__':
  try:
    talker(previousLineCount) 
  except rospy.ROSInterruptException:
    pass
        




