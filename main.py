from output_control import Servo,Stepper,DC
from logic import Gantry_SYS, Claw_SYS
from machine import Pin
import time

led = Pin(15, Pin.OUT)

# GANTRY OBJECTS 
xDC = DC(16,17)
yDC = DC(17,18)
Gantry = Gantry_SYS(xDC,yDC)
# TODO: Create an input handler ->constantly updates a list with events/STATES based off inputs
# TODO: Create a Controller to handle logic based off of state + events 
# TODO: Create a Task Queue that holds taks and has one go at a time

print("test beggining")
while True:
    led.toggle()
    xDC.set_speed(50)
    time.sleep(1)