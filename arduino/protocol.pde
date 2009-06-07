
/** The Arduino will calculate these values for you **/
int direction;      // which direction to move

/* 
   CW = Clockwise
   CCW = Counter clockwise
   PWM CW = PWM clockwise
   PWM CCW = PWM counter clockwise
*/
int pinMotor1 = 5;
int pinMotor2 = 9;

int M1_STOP = 0;
int M1_FULL = 1000;
int M1_STEP = 8;

int M2_STOP = 0;
int M2_FULL = 500;
int M2_STEP = 8;

/* DEBUG */
int ledPin = 13;                // LED connected to digital pin 13

void setup() {
  /* DEBUG */
  pinMode(ledPin, OUTPUT);      // sets the digital pin as output
  
  pinMode(pinMotor1, OUTPUT);
  pinMode(pinMotor2, OUTPUT);
  
  // open serial connection
  Serial.begin(9600);
  
  clear_pins();
}

void loop() {
  // wait for serial input
  if (Serial.available() > 0) {
    direction = Serial.read();
    switch (direction) {
      case 'F':
        move_forward();
        break;
      case 'L':
        move_left();
        break;
      case 'R':
        move_right();
        break;
      default:
        break;
    }
    clear_pins();
  } else {
//    move_forward();
  }
}

void clear_pins() {
  analogWrite(pinMotor1, M1_STOP);
  analogWrite(pinMotor2, M1_STOP);
}

void move_forward() {
  digitalWrite(ledPin, HIGH);
  analogWrite(pinMotor1, M1_FULL);
  analogWrite(pinMotor2, M2_FULL);
  delay(10000);
  analogWrite(pinMotor1, M1_STOP);
  analogWrite(pinMotor2, M2_STOP);  
  digitalWrite(ledPin, LOW);
}

void move_left() {
  digitalWrite(ledPin, HIGH);
  analogWrite(pinMotor2, M2_FULL);
  delay(10000);
  analogWrite(pinMotor2, M2_STOP);  
  digitalWrite(ledPin, LOW);
}

void move_right() {
  digitalWrite(ledPin, HIGH);
  analogWrite(pinMotor1, M1_FULL);
  delay(10000);
  analogWrite(pinMotor1, M1_STOP);  
  digitalWrite(ledPin, LOW);
}
