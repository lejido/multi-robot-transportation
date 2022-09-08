import rospy 
from std_msgs.msg import String

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + "Weight: %s grams", data.data) 

def listener():
  rospy.init_node('loadcellSubscriber', anonymous=True)
  rospy.Subscriber("loadcell", String, callback) 
  rospy.spin() 

if __name__ == '__main__':
  listener()
