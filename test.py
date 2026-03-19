from machine import ADC, Pin
from time import sleep
import neopixel

from output_control import DC, led_strip
from sensors import Joystick,limit_switch,Button

#============= Sensors =================
#Joysticks 
joystick = Joystick(27,28) #Y,X

#limit switch
Chute_lim_switch = limit_switch(0)
#X_lim_switch = limit_switch(2)
#Y_lim_switch = limit_switch(3)

#big beuatiful button: 
button = Button(4)


#============= OUTPUTS ==============

#onboard LED
led = Pin("LED", Pin.OUT)

#servo

#motors 
ZMotor = DC(14,15)
XMotor = DC(12,13)

#led_strip
# led_strip_1 = led_strip(12,1)

# def calibration_sequence():
#     while not X_lim_switch.pressed():
#         XMotor.set_speed(-100)
#     XMotor.stop()
#     while not Z_lim_switch.pressed():
#         ZMotor.set_speed(-100)
#     ZMotor.stop()





while True:
    # if button.pressed():
    #     calibration_sequence()
    led.on()
    x, y = joystick.on() 
    x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
    print("X,y =", x,",", y)
    XMotor.set_speed(y)
    ZMotor.set_speed(x)

    # if Chute_lim_switch.pressed():
    #     led_strip_1.party_time()

    