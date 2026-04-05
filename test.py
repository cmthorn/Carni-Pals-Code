from machine import ADC, Pin, UART
import config
import time
import neopixel

from output_control import DC, led_strip, Servo, Stepper,Speaker
from sensors import Joystick,limit_switch,Button

#============= Sensors =================
#Joysticks 
joystick = Joystick(config.joyVy, config.joyVx) 

#limit switch
Chute_lim_switch = limit_switch(16) #current test switch 
#z_lim_switch = limit_switch(2)
#Y_lim_switch = limit_switch(3)

#big beuatiful button: 
button = Button(config.Button)


#============= OUTPUTS ==============

#SPEAKERS
speaker = Speaker(15) #input busypin laer


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
led = Pin("LED", Pin.OUT)


#motors 
ZMotor = DC(config.ZMotorLPWM,config.ZMotorRPWM)
XMotor = DC(config.XMotorLPWM,config.XMotorRPWM)

#Servo 
ClawServo = Servo(config.servo) 

#led_strip
# led_strip_1 = led_strip(12,1)

stepper = Stepper(config.Stepper1, config.Stepper3,config.Stepper2, config.Stepper4)

count = 0
delay = 1.5

#uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,0x01,0xEF]))  # play 0001.mp3
while True:  
    led.on()
    # speaker.bgMusic()
    # print(speaker.busy())

    # x, y = joystick.on() 
    # x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
    # print("X,y =", x,",", y)
    # XMotor.set_speed(y)
    # ZMotor.set_speed(x)

    # current_time = time.time()
    # if Chute_lim_switch.pressed():
    #     if count1 == 0 and current_time - last_action_time_switch > delay:
    #         print("Worked1")
    #         ClawServo.write(0)
    #         count1 = 1
    #         last_action_time_switch = current_time

    #     elif count1 == 1 and current_time - last_action_time_switch > delay:
    #         print("Worked2")
    #         ClawServo.write(120)
    #         count1 = 0
    #         last_action_time_switch = current_time
    stepper.step(512,-1)

    # if button.pressed():        
    #     if count == 0:
    #         print("Worked1")
    #         stepper.step(100,1)
    #         ClawServo.write(0)
    #         count = 1
    #         time.sleep(0.5)
    #         print("done")
    #     elif count == 1:
    #         print("Worked2")
    #         stepper.step(100,-1)
    #         ClawServo.write(120)
    #         count = 0
    #         time.sleep(0.5)
         

  
    
    # # if button.pressed()==1:
    # #     print("Button Pressed!")

    # # if Chute_lim_switch.pressed():
    # #     led_strip_1.party_time()

    