from output_control import Servo,DC,Speaker,TFF6612FNG
import config
from sensors import limit_switch,Button, Joystick 
from machine import Pin, PWM,ADC, UART
import time

# ~------------------~[OUTPUTS]~-----------------------~
speaker = Speaker(config.busy) #input busypin laer

#========= GANTRY SETUP
#initialize Gantry states and pins 
ZMotor = DC(config.ZMotorLPWM,config.ZMotorRPWM)
XMotor = DC(config.XMotorLPWM,config.XMotorRPWM)


#CLAW
ClawServo = Servo(config.servo) 

YMotor = TFF6612FNG(config.PWMA, config.AIN1, config.AIN2)

#the most important component:
led = Pin("LED", Pin.OUT)

# ~------------------~[INPUTS]~-----------------------~

# =============== USER CONTROLS ====================
joystick = Joystick(config.joyVy, config.joyVx) 
button = Button(config.buttonpin)

#================= Limit switches ==================
z_lim_switch = limit_switch(config.zlimswitch)
x_lim_switch = limit_switch(config.xlimswitch)


# ========== Game States ==========
IDLE = 0
PLAYING = 1
GRABBING = 2
GAME_OVER = 3

state = IDLE

def calibration_sequence(X:DC, Y:DC, limX: limit_switch, LimY:limit_switch):
    x = False
    z = False
    while not x_lim_switch.pressed():
        XMotor.set_speed(-100)
    XMotor.set_speed(0)
    while not z_lim_switch.pressed():
        ZMotor.set_speed(100)
    ZMotor.set_speed(0)
        
        
def grab(): 
    # RESET SUSBSYTEMS
    ZMotor.stop()
    XMotor.stop()
    ClawServo.write(180)

    #LOWER
    print("button presseed lowering")
    YMotor.set_speed(30,-1)
    time.sleep(2)
    YMotor.set_speed(0)
    
    #Close Claw 
    ClawServo.write(0)
    print("servo Closing")
    time.sleep(1.75)

    #UPPIES
    print("Closed, going up")
    YMotor.set_speed(35,1)
    time.sleep(4)
    YMotor.set_speed(0)
    
    #SUCESSEROONIE
    calibration_sequence(XMotor,ZMotor,x_lim_switch,z_lim_switch)
    print("servo Opening")
    ClawServo.write(180)
    time.sleep(1)
    print("done")

count = 0
YMotor.set_speed(0)
while True: 
    led.on()
     # ---- IDLE: wait for player ----
    if state == IDLE:
        
        print("state = idle")
        XMotor.stop()
        ZMotor.stop()
        ClawServo.write(0)  # reset claw

        if button.pressed():
            speaker.bgMusic()         # start music
            state = PLAYING
            count = 1
            time.sleep(0.5)

    # ---- PLAYING: joystick + music ----
    elif state == PLAYING:
        print("state = playing")
        
        x, y = joystick.on() 
        x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
        #print("X,y =", x,",", y) #for debugging
        XMotor.set_speed(y)
        ZMotor.set_speed(x)

        # ready button interrupts music
        if button.pressed():
            speaker.stop()
            state = GRABBING
            time.sleep(0.5)
   
        # song ended naturally
         
        # elif not speaker.is_busy():
        #     speaker.stop()
        #     speaker.failMusic()
        #     state = GAME_OVER

    # ---- GRABBING: claw sequence ----
    elif state == GRABBING:
        print("state = grabbing")
        grab()
        ClawServo.write(180)


        state = GAME_OVER

    # ---- GAME_OVER: reset game ----
    elif state == GAME_OVER:
        print("state = Game Over")
        XMotor.stop()
        ZMotor.stop()
        ClawServo.write(0)
        time.sleep(1)
        state = IDLE

    # ---- small delay for loop ----
    time.sleep(0.01)  # prevents hogging CPU
    
        
  