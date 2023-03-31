#include <VirtualWire.h>
#include <Wire.h> 

#define PIR_Pin 2
#define TX_Pin 3

char *controller;
void setup() {
  pinMode(13,OUTPUT);
  pinMode(2,INPUT);
  vw_set_tx_pin(TX_Pin);
  vw_setup(2000);// speed of data transfer Kbps
}

void loop(){
  
  if(digitalRead(PIR_Pin)==HIGH){
      controller="1" ;
      vw_send((uint8_t *)controller,strlen(controller));
      vw_wait_tx(); 
      digitalWrite(13,1);
      delay(100);
  }
  else{
      controller="0" ;
      vw_send((uint8_t *)controller,strlen(controller));
      vw_wait_tx();
      digitalWrite(13,0);
      delay(100);
  }
}
