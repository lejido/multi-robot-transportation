#include <phidget22.h> 
#include <iostream> 
#include <unistd.h>

using namespace std; 

static void CCONV onVoltageRatioChange(PhidgetVoltageRatioInputHandle ch, void *ctx, double voltageRatio) {
  printf("%s", "hello"); 
  printf("VoltageRatio: %lf\n", voltageRatio); 
}    


int main() {
  PhidgetVoltageRatioInputHandle voltageRatioInput0; 
  
  while(1) {
    cout << "l" << endl; 
    PhidgetVoltageRatioInput_create(&voltageRatioInput0);
    PhidgetVoltageRatioInput_setOnVoltageRatioChangeHandler(voltageRatioInput0, onVoltageRatioChange, NULL);
    Phidget_openWaitForAttachment((PhidgetHandle)voltageRatioInput0, 1000); 
    //time_t start = time(NULL); 
    cout << "s" << endl; 
  } 
  
  Phidget_close((PhidgetHandle)voltageRatioInput0); 
  PhidgetVoltageRatioInput_delete(&voltageRatioInput0);  
  
}
