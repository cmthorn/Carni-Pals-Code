# from machine import UART, Pin
# import time

# uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
# time.sleep(1)  # give DFPlayer time to boot

# uart.write(bytearray([0x7E, 0xFF, 0x06, 0x03, 0x00, 0x00, 0x01, 0xEF]))

# time.sleep(50)

from machine import Pin
from time import sleep

p = Pin(20, Pin.IN, Pin.PULL_UP)

while True:
    print(p.value())
    sleep(0.2)


