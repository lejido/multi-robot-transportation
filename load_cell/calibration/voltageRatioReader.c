#include <phidget22.h>
#include <stdio.h> 
#include <unistd.h> 
#include <time.h>
#include <string.h> 
#include <stdlib.h> 
#define Sleep(x) usleep((x) * 1000)

// declare event handlers here 

int inc = 0; 
double sum = 0.0; 

static void CCONV onVoltageRatioChange(PhidgetVoltageRatioInputHandle ch, void * ctx, double voltageRatio) {
  printf("VoltageRatio: %lf\n", voltageRatio); 
  //inc++;
  //sum += voltageRatio; 
  
  // printf("Weight: %lf\n", m_cal * (voltageRatio-(-0.000087)));
  FILE *fp; 
  fp = fopen("data.txt", "a+"); 
  char output[10]; 
  snprintf(output, 10, "%f", voltageRatio); 

  char entry[12]; 
  strcpy(entry, output);
  strcat(entry, "\n"); 
  
  if (fp) {
    fputs(entry, fp); 
  } else {
    printf("%s", "File not reachable.\n"); 
  }
  fclose(fp);    

}

int main() {
  
  // declare phidget channels and other vars
  PhidgetVoltageRatioInputHandle voltageRatioInput0; 
  
  time_t endwait; 
  time_t start = time(NULL); 
  time_t seconds = 10; 

  endwait = start+seconds; 

  //while (start < endwait) {
  while(1) { 
    // create channels 
    PhidgetVoltageRatioInput_create(&voltageRatioInput0); 

    // set addressing params to specify which channel to open (if any) 

    // assign any event handlers required before calling open so that no events are missed 
    PhidgetVoltageRatioInput_setOnVoltageRatioChangeHandler(voltageRatioInput0, onVoltageRatioChange, NULL); 

    // open phidgets and wait for attachment
    Phidget_openWaitForAttachment((PhidgetHandle)voltageRatioInput0, 5000); 
  
    // do stuff with phidgets here or in event handlers 
  
    // Sleep(5000);
    sleep(1); 
    start = time(NULL); 
  }

  // close phidgets once program is done 
  Phidget_close((PhidgetHandle)voltageRatioInput0); 

  PhidgetVoltageRatioInput_delete(&voltageRatioInput0); 
  // fclose(fptr);

  //printf("Weight: %lf", );
  fclose(fopen("data.txt","w")); 
}
