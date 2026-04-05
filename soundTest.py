from machine import UART
from time import sleep
uart = UART(0, baudrate=9600, tx=0, rx=1)

while True: 
    uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,0x01,0xEF]))  # play 0001.mp3
    sleep(44)
    break

