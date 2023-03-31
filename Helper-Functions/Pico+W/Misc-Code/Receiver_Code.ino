#include <VirtualWire.h>
#include <Wire.h> 


#define RX_Pin 2


int off = 0;

void setup(){
  pinMode(13,OUTPUT);
  digitalWrite(13, LOW);;
  
  vw_set_rx_pin(RX_Pin);
  vw_setup(2000); 
  vw_rx_start(); 
  
}
void loop(){
  uint8_t buf[VW_MAX_MESSAGE_LEN];
  uint8_t buflen = VW_MAX_MESSAGE_LEN;

  if (vw_get_message(buf, &buflen)){
    if(buf[0]=='0'){
    digitalWrite(13,0);
      off = 1;
    } 
    if(buf[0]=='1'){
    digitalWrite(13,1);
    }
  }
}
