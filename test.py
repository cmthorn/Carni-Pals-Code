from machine import ADC, Pin, UART
import config
import time
import neopixel

from output_control import DC, led_strip, Servo, Stepper,Speaker,TFF6612FNG
from sensors import Joystick,limit_switch,Button

#============= Sensors =================
#Joysticks 
joystick = Joystick(config.joyVy, config.joyVx) 

#limit switch
#Chute_lim_switch = limit_switch(config.limswitchchute) #current test switch 
z_lim_switch = limit_switch(config.zlimswitch)
x_lim_switch = limit_switch(config.xlimswitch)

#big beuatiful button: 
button = Button(config.buttonpin)
#p = Pin(20, Pin.IN, Pin.PULL_UP)

#============= OUTPUTS ==============

#SPEAKERS
speaker = Speaker(config.busy) 


def play(track_number):
    """
    Play track by number
    track_number: integer (1,2,3,...)
    """
    #
    command = bytearray([
        0x7E,      # start byte
        0xFF,      # version
        0x06,      # length
        0x03,      # command: play track
        0x00,      # feedback: 0=no, 1=yes
        0x00,      # high byte of track
        track_number, # low byte of track
        0xEF       # end byte
    ])
    uart.write(command)


#onboard LED
led = Pin(0, Pin.OUT)


#motors 
ZMotor = DC(config.ZMotorLPWM,config.ZMotorRPWM)
XMotor = DC(config.XMotorLPWM,config.XMotorRPWM)
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
while True:  
    if button.pressed():
        if count == 0: 
            print("openning")
            ClawServo.write(180)
            time.sleep(1)
            count = 1

    time.sleep(0.25)
    if button.pressed():
        if count == 1: 
            print("closing")
            ClawServo.write(0)
            time.sleep(1)
            count = 0
    
    #print("Z:",z_lim_switch.pressed(),"| X:",x_lim_switch.pressed())
    # x, y = joystick.on() 
    # x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
    # print("X,y =", x,",", y) #for debugging
        
    # if button.pressed():
    #     if count == 0: 
    #         YMotor.set_speed(30,-1)
    #         time.sleep(1.5)
    #         YMotor.set_speed(0)
    #         count = 1
    #         time.sleep(1)

    # if button.pressed():
    #     if count == 1: 
    #         YMotor.set_speed(35,1)
    #         time.sleep(3)
    #         YMotor.set_speed(0)
    #         count = 0
    #         time.sleep(1)

    # YMotor.set_speed(30,-1)
    # time.sleep(1)
    # YMotor.set_speed(0)
    # time.sleep(60)
    # YMotor.set_speed(30,1)
    # time.sleep(1.5)
    # YMotor.set_speed(0)
    # time.sleep(2)
  
    
    led.on()


    