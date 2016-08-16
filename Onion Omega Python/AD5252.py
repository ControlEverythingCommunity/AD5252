# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AD5252
# This code is designed to work with the AD5252_I2CPOT_10K I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Potentiometers?sku=AD5252_I2CPOT_10K#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# AD5252 address, 0x2C(44)
# Send instruction for POT channel-0, 0x01(01)
#		0x80(128)	Input resistance value
data = [0x80]
i2c.writeBytes(0x2C, 0x01, data)
# AD5252 address, 0x2C(44)
# Send instruction for POT channel-1, 0x03(03)
#		0x80(128)	Input resistance value
data = [0x80]
i2c.writeBytes(0x2C, 0x03, data)

time.sleep(0.5)

# AD5252 address, 0x2C(44)
# Read data back from 0x01(01), 1 byte
data = i2c.readBytes(0x2C, 0x01, 1)

# Convert the data
res_1 = (data / 256.0 ) * 10.0

# AD5252 address, 0x2C(44)
# Read data back from 0x03(03), 1 byte
data = i2c.readBytes(0x2C, 0x03, 1)

# Convert the data
res_2 = (data / 256.0 ) * 10.0

# Output data to screen
print "Resistance Channel-0 : %.2f K" %res_1
print "Resistance Channel-1 : %.2f K" %res_2
