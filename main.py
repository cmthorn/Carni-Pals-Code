from output_control import Servo,Stepper,DC
from machine import Pin
import time

led = Pin(15, Pin.OUT)
xDC = DC(16,17)

print("test beggining")
while True:
    led.toggle()
    xDC.set_speed(50)
    time.sleep(1)