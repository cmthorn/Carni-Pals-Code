from output_control import Servo,Stepper,DC
from sensors import limit_switch
from logic import DCMotorState, State, Controller
from machine import Pin
import time

led = Pin(25, Pin.OUT)

#initialize Gantry states and pins 
xDC = DC(16,17)
yDC = DC(18,19)



#initialize all sensors 
testLimSwitch = limit_switch(0)
testLimSwitch2 = limit_switch(1)
brain = Controller( xDC, yDC, testLimSwitch, testLimSwitch2)


          

print("test beggining")
tasks = {}
while True:
    led.on()
    brain.update()
    # led.toggle()
    # xDC.set_speed(50)
    # time.sleep(1)