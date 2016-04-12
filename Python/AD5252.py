# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD5252
# This code is designed to work with the AD5252_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Potentiometers?sku=AD5252_I2CPOT_10K#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# AD5252 address, 0x2C(44)
# Send instruction for POT channel-0, 0x01(01)
#		0x80(128)	Input resistance value
bus.write_i2c_block_data(0x2C, 0x01, [0x80])
# AD5252 address, 0x2C(44)
# Send instruction for POT channel-1, 0x03(03)
#		0x80(128)	Input resistance value
bus.write_i2c_block_data(0x2C, 0x03, [0x80])

time.sleep(0.5)

# AD5252 address, 0x2C(44)
# Read data back from 0x01(01), 1 byte
data = bus.read_byte_data(0x2C, 0x01)

# Convert the data
res_1 = (data / 256.0 ) * 10.0

# AD5252 address, 0x2C(44)
# Read data back from 0x03(03), 1 byte
data = bus.read_byte_data(0x2C, 0x03)

# Convert the data
res_2 = (data / 256.0 ) * 10.0

# Output data to screen
print "Resistance Channel-0 : %.2f K" %res_1
print "Resistance Channel-1 : %.2f K" %res_2
