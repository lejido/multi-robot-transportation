#include <phidget22.h> 
#include <stdio.h>
#include <unistd.h> 
#include <time.h> 
#include <string.h> 
#include <stdlib.h> 
#include "ros/ros.h" 
#include "std_msgs/Float32.h" 
#include <sstream> 

using namespace std; 

void loadCellCallback(const std_msgs::Float32::ConstPtr& payloadWeight) {
  ROS_INFO("Weight: %lf", payloadWeight->data);  
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "listener"); 
  ros::NodeHandle n; 
  ros::Subscriber sub = n.subscribe("loadCell", 1000, loadCellCallback); 
  ros::spin(); 
  return 0; 
}

