# keypress version with matplotlib
"""
F = (R-0.0033)*10
R0 = 0.0033, F1 = 0 
             F = 200
(f1-f0)/(r1-r0) = 10
F = 200 


Here are some ideas for debugging this:
Test the python script for bugs. You could generate some fake data from a linear function [e.g., assume F = (R-0.0033)*10. Draw some data points from this function. Feed them to the python script, and see if your script would give back the correct values]
non-linearity does exist but locally the load cell would behave linearly, so for small change in F, the linear model should hold.
I would try to make sure the script is bug free before exploring other stuff

"""

# run once for F0 and F1 for calibration
import keyboard 
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
# import rospy 
# from std_msgs.msg import String # this probably nears to be an int msg 
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time 

# fig = plt.figure() 
# ax1 = fig.add_subplot(1,1,1) 

"""
def animate():
  data = open("data.txt","r").read()
  arr = data.split('\n')
  x = [] 
  y = [] 
  for line in arr:
    if (len(line)>1):
      xc, yc = line.split(',') 
      x.append(int(xc))
      y.append(int(yc))
  ax1.clear() 
  ax1.plot(x, y) 
"""

sm  = 0 
inc = 0 
def onVoltageRatioChange(self, voltageRatio):
  #print("VoltageRatio: " + str(voltageRatio))
  # talker(voltageRatio)
  gr = (voltageRatio+0.0880673458278493)*(-15646.85594709813)
  print(gr)
  gr2 = (voltageRatio+0.02604019549956554)*-37614.20678828169
  print(gr2)
  global sm, inc
  sm += voltageRatio
  inc += 1 
  # f = open("data.txt", "a")
  # print(type(voltageRatio)) 
  
  # f.write(str(voltageRatio) + '\n')
  # f.close()
  #ani = animation.FuncAnimation(fig, animate, interval=1000) 
  #plt.show()
   

def talker(data):
  pub = rospy.Publisher('topic_voltageRatio', String, queue_size=10) # replace string with int msg 
  rospy.init_node('talker', anonymous=True) 
  rate = rospy.Rate(10) 
  while not rospy.is_shutdown():
    voltageRatio = data  
    rospy.loginfo(data + " " + str(rospy.get_time())) 
    pub.publish(voltageRatio) 
    rate.sleep() 

#time = 30 
#timeout_start = time.time() 

# while time.time() < timeout_start + timeout:

voltageRatioInput0 = VoltageRatioInput()
while inc<1000:
  if (keyboard.is_pressed('q')):    
    voltageRatioInput0 = VoltageRatioInput()
    voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioChange) 
    voltageRatioInput0.openWaitForAttachment(1000)
  elif (keyboard.is_pressed('p')): 
    voltageRatioInput0.close() 
    break

print(sm)
print(inc)

"""
data = open("data.txt","r").read() 
arr = data.split('\n')
sm = 0 
for i in arr:
  sm += float(i)

print("Avg: " + str(sm/len(arr)))

"""













 
