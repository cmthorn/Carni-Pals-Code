from motor_control import Servo,Stepper,DC
from machine import Pin
import time

led = Pin(25, Pin.OUT)

print("test beggining")
while True:
    led.toggle()
    time.sleep(0.5)