int incomingByte = 0;
int pin = 13;

void setup() {
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW); 
  Serial.begin(115200);
}

void loop() {  
  while(Serial.available() > 0) {     
      char aChar = Serial.read();
      if(aChar == '\n') {
        digitalWrite(pin, HIGH);
        delay(80);
        digitalWrite(pin, LOW);
      }  
   }
}




