from output_control import Servo,Stepper,DC
from sensors import limit_switch,Button, Joystick 
from logic import DCMotorState, State, Controller
from machine import Pin,PWM,ADC 
import time


#initialize Gantry states and pins 
xDC = DC(16,17)# DO MORE TESTING ON XDC -> CURRENTLY NOT FUNCTIONING
yDC = DC(18,19)

joystick = Joystick(27,26)

#Initialize claw components 
ArcadeClaw = Servo(11)
A_button = Button(4)

#initialize all sensors 
testLimSwitch = limit_switch(0)
testLimSwitch2 = limit_switch(1)
brain = Controller( xDC, yDC, testLimSwitch, testLimSwitch2)


print("begin testing")     

led = Pin("LED", Pin.OUT)
led2 = Pin(15, Pin.OUT)
state = 1

while True:
    led.on()
    # print(joystick.check_axis())
    if A_button.pressed() == 0: 
        print("button pressed")
        if state == 1: 
            ArcadeClaw.write(180)
            
        else:
            ArcadeClaw.write(0)
        state *= -1 
        time.sleep(1)
        
  