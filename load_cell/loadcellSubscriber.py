import rospy 
from std_msgs.msg import Float32

def callback(data):
  rospy.loginfo(rospy.get_caller_id() + "Weight: %lf grams", data.data) 

def listener():
  rospy.init_node('loadcellSubscriber', anonymous=True)
  rospy.Subscriber("loadcell", Float32, callback) 
  rospy.spin() 

if __name__ == '__main__':
  listener()
