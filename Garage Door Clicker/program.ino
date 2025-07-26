#define BLYNK_TEMPLATE_ID "------------"
#define BLYNK_TEMPLATE_NAME "Garage Door"
#define BLYNK_AUTH_TOKEN "----------------"

#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <ESP32Servo.h>

// WiFi credentials
char ssid[] = "-------";
char pass[] = "-------";

// Servo
Servo servo;
const int servoPin = 22;

// Battery voltage reading
const int batteryPin = 33;

// LED Pins
const int redLED = 21;
const int yellowLED = 19;
const int greenLED = 18;

// Battery thresholds (adjust based on your divider and battery voltage range)
float lowThreshold = 3.3;
float midThreshold = 3.7;

BLYNK_WRITE(V2) {
  int buttonState = param.asInt();
  if (buttonState == 1) {
    servo.attach(servoPin);
    servo.write(180);  // Simulate button press
    delay(3000);

    servo.write(180);   // Reset
    delay(600);

    servo.write(60);   // Stop
    delay(300);

    servo.detach();
  }
}

void setup() {
  Serial.begin(115200);

  // Start Blynk
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  // Initialize LED pins
  pinMode(redLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(greenLED, OUTPUT);

  // Start with all LEDs off
  digitalWrite(redLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(greenLED, LOW);
}

void loop() {
  Blynk.run();
  checkBatteryAndIndicate();
}

void checkBatteryAndIndicate() {
  int raw = analogRead(batteryPin);
  float voltage = (raw / 4095.0) * 3.3 * 2;  // 3.3V ref, 100k:100k divider
  Serial.print("Battery voltage: ");
  Serial.println(voltage, 2);

  // Turn off all LEDs first
  digitalWrite(redLED, LOW);
  digitalWrite(yellowLED, LOW);
  digitalWrite(greenLED, LOW);

  // Indicate battery level
  if (voltage < lowThreshold) {
    digitalWrite(redLED, HIGH);
  } else if (voltage < midThreshold) {
    digitalWrite(yellowLED, HIGH);
  } else {
    digitalWrite(greenLED, HIGH);
  }

  delay(1000);  // Check once per second
}
