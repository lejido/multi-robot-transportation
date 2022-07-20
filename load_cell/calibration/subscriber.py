import rospy 
from std_msgs.msg import String # change msg type 

cnt= 0 
voltageRatioSum = 0 

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + "Received data %s", data.data) # change for msg type not string 
  voltageRatioSum += data.data # change for msg type 
  cnt += 1


def listener():
  rospy.init_node('listener', anonymous=True) 
  rospy.Subscriber('topic_voltageRatio', String, callback) 
  rospy.spin()

listener() 

