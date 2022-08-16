#include "HX711.h"

#define calibration_factor 2200.0 

#define DOUT  3
#define CLK  2

HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); 
  scale.tare(); 
}

void loop() {
  Serial.println(scale.get_units(), 4); 
}

