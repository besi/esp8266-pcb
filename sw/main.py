from machine import Pin, SoftI2C
from hdc1080 import HDC1080

scl = Pin(14, Pin.IN, Pin.PULL_UP)
sda = Pin(2, Pin.IN, Pin.PULL_UP)

i2c = SoftI2C(scl,sda)
temp = HDC1080(i2c)

print(temp.temperature())
print(temp.humidity())

 
from neopixel import NeoPixel
np = NeoPixel(Pin(4),1)
np[0] = (1, 2, 5)

np.write()
