// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// AD5252
// This code is designed to work with the AD5252_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Potentiometers?sku=AD5252_I2CPOT_10K#tabs-0-product_tabset-2

#include <application.h>
#include <spark_wiring_i2c.h>

// AD5252 I2C address is 0x2C(44)
#define Addr 0x2C

float res_1 = 0.0, res_2 = 0.0;
void setup()
{
  // Set variable
  Particle.variable("i2cdevice", "AD5252");
  Particle.variable("res_1", res_1);
  Particle.variable("res_2", res_2);

  // Initialise I2C communication as Master
  Wire.begin();
  // Initialise serial communication, set baud rate = 9600
  Serial.begin(9600);

  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Send instruction for POT channel-0
  Wire.write(0x01);
  // Input resistance value, 0x80(128)
  Wire.write(0x80);
  // Stop I2C transmission
  Wire.endTransmission();

  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Send instruction for POT channel-1
  Wire.write(0x03);
  // Input resistance value, 0x80(128)
  Wire.write(0x80);
  // Stop I2C transmission
  Wire.endTransmission();
  delay(300);
}

void loop()
{
  unsigned int data;

  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x01);
  // Stop I2C transmission
  Wire.endTransmission();

  // Request 1 byte of data
  Wire.requestFrom(Addr, 1);

  // Read 1 byte of data
  if (Wire.available() == 1)
  {
    data = Wire.read();
  }

  // Convert the data
  res_1 = (data / 256.0 ) * 10.0;

  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Select data register
  Wire.write(0x03);
  // Stop I2C transmission
  Wire.endTransmission();

  // Request 1 byte of data
  Wire.requestFrom(Addr, 1);

  // Read 1 byte of data
  if (Wire.available() == 1)
  {
    data = Wire.read();
  }

  // Convert the data
  res_2 = (data / 256.0 ) * 10.0;

  // Output data to dashboard
  Particle.publish("Resistance Channel-0 : ", String(res_1) + " K");
  Particle.publish("Resistance Channel-1 : ", String(res_2) + " K");
  delay(500);
}
