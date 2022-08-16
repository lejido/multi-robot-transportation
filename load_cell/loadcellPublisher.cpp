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

double voltageRatioReading = 0.0; 

static void CCONV onVoltageRatioChange(PhidgetVoltageRatioInputHandle ch, void * ctx, double voltageRatio) {
  voltageRatioReading = voltageRatio; 
}

int main(int argc, char **argv) {

  ros::init(argc, argv, "talker"); 
  ros::NodeHandle n; 
  ros::Publisher loadCellPub = n.advertise<std_msgs::Float32>("loadCell", 1000); 
  ros::Rate loop_rate(10); 
  
  PhidgetVoltageRatioInputHandle voltageRatioInput0; 


  while(ros::ok()) {
    std_msgs::Float32 payloadWeight; 

    PhidgetVoltageRatioInput_create(&voltageRatioInput0); 
    PhidgetVoltageRatioInput_setOnVoltageRatioChangeHandler(voltageRatioInput0, onVoltageRatioChange, NULL); 
    Phidget_openWaitForAttachment((PhidgetHandle)voltageRatioInput0, 5000); 
    sleep(1); 
    
    payloadWeight.data = voltageRatioReading * 9.92301036e+05 + -3.35582650e+01; 
    ROS_INFO("%lf", payloadWeight.data); 
    
    loadCellPub.publish(payloadWeight); 
    
    ros::spinOnce(); 

    loop_rate.sleep(); 
  }
  
  return 0; 
}

