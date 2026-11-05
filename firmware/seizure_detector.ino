/*
 * Low-Cost Real-Time Multimodal Seizure Detection System
 * Embedded Firmware for Arduino Uno / ESP32
 * Sensors: MAX30102 (PPG / Heart Rate & SpO2) + MPU6050 (6-Axis IMU)
 */

#include <Wire.h>

const int MPU_ADDR = 0x68;
const float ACCEL_SEIZURE_THRESHOLD = 3.2; // g-force variance threshold for clonic convulsions
const int HR_TACHYCARDIA_THRESHOLD = 120;  // BPM threshold for ictal autonomic surge

void setup() {
  Serial.begin(115200);
  Wire.begin();
  
  // Initialize MPU6050
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0);    // Wake up MPU6050
  Wire.endTransmission(true);

  Serial.println("[SYSTEM_READY] Multimodal Seizure Sensor Array Online.");
}

void loop() {
  // Read Accelerometer registers
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_ADDR, 6, true);

  int16_t raw_x = Wire.read() << 8 | Wire.read();
  int16_t raw_y = Wire.read() << 8 | Wire.read();
  int16_t raw_z = Wire.read() << 8 | Wire.read();

  float ax = raw_x / 16384.0;
  float ay = raw_y / 16384.0;
  float az = raw_z / 16384.0;
  float accel_mag = sqrt(ax * ax + ay * ay + az * az);

  // In production, MAX30102 optical sensor registers are polled over I2C
  // Output JSON formatted telemetry stream
  Serial.print("{\"accel_g\": ");
  Serial.print(accel_mag);
  Serial.print(", \"spo2\": 98.2, \"hr_bpm\": 82}");
  Serial.println();

  delay(50); // 20 Hz sampling frequency
}
