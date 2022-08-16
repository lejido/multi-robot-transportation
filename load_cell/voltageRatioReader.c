#include <phidget22.h>
#include <stdio.h> 
#include <unistd.h> 
#include <time.h>
#include <string.h> 
#include <stdlib.h> 

static void CCONV onVoltageRatioChange(PhidgetVoltageRatioInputHandle ch, void * ctx, double voltageRatio) {
  printf("VoltageRatio: %lf\n", voltageRatio); 
  // double f = (voltageRatio * 1.01297885e+06 + 9.77941741e+01) * 9.81 ;
  double f = (voltageRatio * 9.92301036e+05 + -3.35582650e+01); 
  printf("Weight: %lf grams\n", f); 
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
  
  PhidgetVoltageRatioInputHandle voltageRatioInput0; 
  
  time_t endwait; 
  time_t start = time(NULL); 
  time_t seconds = 10; 
  
  endwait = start+seconds; 
  
  //while (start < endwait) {
  while(1) {
    PhidgetVoltageRatioInput_create(&voltageRatioInput0); 

    PhidgetVoltageRatioInput_setOnVoltageRatioChangeHandler(voltageRatioInput0, onVoltageRatioChange, NULL); 

    Phidget_openWaitForAttachment((PhidgetHandle)voltageRatioInput0, 5000); 
  
    sleep(1); 
    start = time(NULL); 
  }

  Phidget_close((PhidgetHandle)voltageRatioInput0); 

  PhidgetVoltageRatioInput_delete(&voltageRatioInput0); 
  
  fclose(fopen("data.txt","w")); 
}
