#include <Servo.h>

Servo servoX, servoY;
int servoXPin = 11, servoYPin = 12;

int currentAngleX = 90, currentAngleY = 0;

void setup() {
  servoX.attach(servoXPin);
  servoY.attach(servoYPin);
  servoX.write(currentAngleX);
  servoY.write(currentAngleY);
  Serial.begin(250000);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');
    if (commaIndex != -1) {
      int errorX = data.substring(0, commaIndex).toInt();
      int errorY = data.substring(commaIndex + 1).toInt();

      while (abs(errorX) > 20) {
        currentAngleX = constrain(currentAngleX + (errorX > 0 ? 1 : -1), 0, 180);
        servoX.write(currentAngleX);
        delay(15);
        errorX += (errorX > 0 ? -20 : 20);
      }

      while (abs(errorY) > 20) {
        currentAngleY = constrain(currentAngleY + (errorY > 0 ? 1 : -1), 0, 180);
        servoY.write(currentAngleY);
        delay(15);
        errorY += (errorY > 0 ? -20 : 20);
      }
    }
  }
}
