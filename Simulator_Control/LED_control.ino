/* Code for controlling the LEDDriverPCB with an Arduino */

int CH_UV = 3;     // Ultra violet LED connected to digital pin 9
int CH_White = 6; // White LED
int CH_Green = 5; // Green LED
int CH_Red = 9;   // Red LED
int CH_IR = 10;    // Infra red LED

int BT1 = A1; // Button 1
int BT2 = A2;
int BT3 = A3;

int button1 = 0;
int button2 = 0;
int button3 = 0;

float I_UV = 10.0; // percent
float I_White = 10.0;
float I_Green = 10.0;
float I_Red = 10.0;
float I_IR = 10.0;

int state = 2;

void setCustomSpec() {
  I_UV = 0.0; // percent
  I_White = 0.0;
  I_Green = 60.0;
  I_Red = 0.0;
  I_IR = 0.0;
}

void setAM15G() {
  I_UV = 80.0; // percent
  I_White = 40.0;
  I_Green = 30.0;
  I_Red = 100.0;
  I_IR = 50.0; // infrared limit is 50%
}

void setAM0() {
  I_UV = 10.0; // percent
  I_White = 15.0;
  I_Green = 12.0;
  I_Red = 11.0;
  I_IR = 10.0;
}
void setZeroSpec() {
  I_UV = 0.0; // percent
  I_White = 0.0;
  I_Green = 0.0;
  I_Red = 0.0;
  I_IR = 0.0;  
}

float getPWMfromPercent(float percent) {
  return 255*percent/100;
}

void setup() {
  Serial.begin(9600);
  pinMode(BT1, INPUT);
  pinMode(BT2, INPUT);
  pinMode(BT3, INPUT);
}

void loop() {
  button1 = digitalRead(BT1);
  button2 = digitalRead(BT2);
  button3 = digitalRead(BT3);
  
  //the big if-machine
  if(button1 == LOW && button2 == LOW && button3 == LOW) {
    Serial.write("LOW\n");
    state = 0;
  }
  else if(button1 == HIGH && button2 == LOW && button3 == LOW) {
    Serial.write("Button 1 high\n");
    state = 1; //AM15
  }
  else if(button1 == LOW && button2 == HIGH && button3 == LOW) {
    Serial.write("Button 2 high\n");
    //state = 2; //AM0
    state = 0;
  }
    else if(button1 == LOW && button2 == LOW && button3 == HIGH) {
    Serial.write("Button 3 is so high richt now\n");
    state = 3; //custom
  }
  else if(button1 == HIGH && button2 == HIGH && button3 == LOW) {
    Serial.write("Button 1 and 2 high\n");
    state = 0;
  }
  else if(button1 == HIGH && button2 == LOW && button3 == HIGH) {
    Serial.write("Button 1 and 3 high\n");
    state = 0;
  }
  else if(button1 == LOW && button2 == HIGH && button3 == HIGH) {
    Serial.write("Button 2 and 3 are surfing on some damn fine clouds\n");
    state = 0;
  }
  else if(button1 == HIGH && button2 == HIGH && button3 == HIGH) {
    Serial.write("EMERGENCY DISCO BUTTON ACTIVATED. Unfortunately does nothing, yet.\n");
    state = 0;
  }

  switch(state) {
    case 0:
      setZeroSpec();
      break;
    case 1:
      setAM15G();
      break;
    case 2:
      setAM0();
      break;
    case 3:
      setCustomSpec();
      break;
  }

  analogWrite(CH_UV, getPWMfromPercent(I_UV));
  analogWrite(CH_White, getPWMfromPercent(I_White));
  analogWrite(CH_Green, getPWMfromPercent(I_Green));
  analogWrite(CH_Red, getPWMfromPercent(I_Red));
  analogWrite(CH_IR, getPWMfromPercent(I_IR));

  delay(1);
  //for(;;){} // 1ms delay for stability
}

