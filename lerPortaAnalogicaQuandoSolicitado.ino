const int potenciometro = 0; // pino de entrada do potenciômetro
float valAnalog = 0;
float temp = 0;
 
void setup() {
  Serial.begin(9600);
  delay(1000);
}
 
void loop() {    
  if (Serial.available() > 0){
    if (Serial.read() == 116){ 
      valAnalog = analogRead(potenciometro);
      temp = (valAnalog * 5) / 1023;
      Serial.println(temp);
      delay(1000);
    }  
  }
}
