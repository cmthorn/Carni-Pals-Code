from machine import ADC, Pin, UART
import config
import time
import neopixel

from output_control import DC, led_strip, Servo, Stepper,Speaker,TFF6612FNG,L289N
from sensors import Joystick,limit_switch,Button

#============= Sensors =================
#Joysticks 
joystick = Joystick(config.joyVy, config.joyVx) 

#limit switch
#Chute_lim_switch = limit_switch(config.limswitchchute) #current test switch 
z_lim_switch = limit_switch(config.zlimswitch)
x_lim_switch = limit_switch(config.xlimswitch)
chute_lim_switch = limit_switch(config.chutelimswitch)

#big beuatiful button: 
button = Button(config.buttonpin)
#p = Pin(20, Pin.IN, Pin.PULL_UP)

#============= OUTPUTS ==============

#SPEAKERS
speaker = Speaker(config.busy) 



#onboard LED
led = Pin(25, Pin.OUT)


#motors 
ZMotor = L289N(config.ZMotorLPWM,config.ZMotorRPWM)
XMotor = L289N(config.XMotorLPWM,config.XMotorRPWM)
#Servo 
ClawServo = Servo(config.servo) 

#led_strip
# led_strip_1 = led_strip(12,1)


    


YMotor = TFF6612FNG(config.PWMA, config.AIN1, config.AIN2)

#directions:
#  1 = counter clockwise -> up 
#  -1 = clockwise -> down

# YMotor.set_speed(30,1)
# time.sleep(3)
 
count = 0
XMotor.set_speed(0)
ZMotor.set_speed(0)


while True:  

    if chute_lim_switch.pressed():
        
    # if button.pressed():
    #     print(button.pressed())

    #     ZMotor.set_speed(0)
    #     XMotor.set_speed(0)
    #     ClawServo.write(180)
    #     time.sleep(2)

    #     #LOWER
    #     print("button presseed lowering")
    #     YMotor.set_speed(30,-1)
    #     time.sleep(2)
    #     YMotor.set_speed(0)
        
    #     #Close Claw 
    #     ClawServo.write(0)
    #     print("servo Closing")
    #     time.sleep(1.75)

    #     #UPPIES
    #     print("Closed, going up")
    #     YMotor.set_speed(35,1)
    #     time.sleep(4)
    #     YMotor.set_speed(0)

    
    led.on()




    