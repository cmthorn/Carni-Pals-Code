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
led = Pin("LED", Pin.OUT)


#motors 
ZMotor = DC(config.ZMotorLPWM,config.ZMotorRPWM)
XMotor = DC(config.XMotorLPWM,config.XMotorRPWM)

#Servo 
ClawServo = Servo(config.servo) 

#led_strip
# led_strip_1 = led_strip(12,1)

stepper = Stepper(config.Stepper1, config.Stepper2, config.Stepper3, config.Stepper4)

count = 0
delay = 1.5


def grab(): 
    ZMotor.stop()
    XMotor.stop()
    ClawServo.write(180)
    print("button presseedm lowering")
    stepper.step(1024,1)
    ClawServo.write(0)
    print("servo Closing")
    time.sleep(1.75)
    print("Closed, going up")
    stepper.step(1024,-1)
    ClawServo.write(180)
    print("servo Opening")
    time.sleep(1)
    print("done")
    

    





speaker.bgMusic()
while True:  
    #print(x_lim_switch.pressed(), ";", z_lim_switch.pressed())
    led.on()
    if button.pressed():
        grab()

    print("limx:", x_lim_switch.pressed()," ; ", "limz:", z_lim_switch.pressed())
    # ClawServo.write(0)
    # time.sleep(1.5)
    # ClawServo.write(180)
    # time.sleep(1.5)

    # x, y = joystick.on() 
    # x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
    # print("X,y =", x,",", y) #for debugging
    #XMotor.set_speed(y)
    #ZMotor.set_speed(x)

    # stepper.step(512,-1)
    # time.sleep(0.5)
    # stepper.step(512,1)
    # time.sleep(1)

# led1 = led_strip(12,config.ledpin)
# led1.party_time()