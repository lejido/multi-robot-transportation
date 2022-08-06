#include <phidget22.h>
#include <stdio.h> 
#include <unistd.h> 
#include <time.h>
#include <string.h> 
#include <stdlib.h> 

extern "C" {
  static void CCONV onVoltageRatioChange(PhidgetVoltageRatioInputHandle ch, void * ctx, double voltageRatio) {
    printf("VoltageRatio: %lf\n", voltageRatio); 
    
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
    printf("%s", "Hello");   
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
    
    // fclose(fptr);
    fclose(fopen("data.txt","w")); 
  }
}
