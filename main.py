from output_control import Servo,Stepper,DC,Speaker
from sensors import limit_switch,Button, Joystick 
from logic import DCMotorState, State, Controller
from machine import Pin, PWM,ADC, UART
import time

# ~------------------~[OUTPUTS]~-----------------------~
speaker = Speaker(0,1,15) #input busypin laer

#========= GANTRY SETUP
#initialize Gantry states and pins 
xDC = DC(16,17)# DO MORE TESTING ON XDC -> CURRENTLY NOT FUNCTIONING
yDC = DC(18,19)

#CLAW
ArcadeClaw = Servo(11)

#the most important component:
led = Pin("LED", Pin.OUT)

# ~------------------~[INPUTS]~-----------------------~

# =============== USER CONTROLS ====================
joystick = Joystick(27,26)
A_button = Button(4)
Start_button = Button(5)

#================= Limit switches ==================
XLimSwitch = limit_switch(6)
ZLimSwitch = limit_switch(7)
Chute_lim_switch = limit_switch(9)

# ========== Game States ==========
IDLE = 0
PLAYING = 1
GRABBING = 2
GAME_OVER = 3

state = IDLE

def calibration_sequence(X:DC, Y:DC, limX: limit_switch, LimY:limit_switch):
    while True:
        if limX.pressed():
            X.set_speed(0)
        else: 
            X.set_speed(100)
        
        if limY.pressed():
            Y.set_speed(0)
        else: 
            Y.set_speed(100)
        
        if limX.pressed() and limY.pressed():
            break
        


while True:
    led.on()
     # ---- IDLE: wait for player ----
    if state == IDLE:
        XMotor.stop()
        ZMotor.stop()
        ClawServo.write(0)  # reset claw

        if start_button.value():
            speaker.bgMusic()         # start music
            state = PLAYING

    # ---- PLAYING: joystick + music ----
    elif state == PLAYING:
        x, y = joystick.on() 
        x, y = joystick.drift_fix(x,y) # fixes non-zero 0 values (e.g. - 0.2)
        #print("X,y =", x,",", y) #for debugging
        XMotor.set_speed(y)
        ZMotor.set_speed(x)

        # ready button interrupts music
        if A_button.value():
            speaker.stop()
            state = GRABBING
        # song ended naturally
        elif speaker.music_over():
            speaker.stop()
            speaker.failMusic()
            state = GAME_OVER

    # ---- GRABBING: claw sequence ----
    elif state == GRABBING:
        XMotor.stop()
        ZMotor.stop()
        # close claw
        ClawServo.write(120)
        sleep(1.5)  # brief delay for claw to close

        # lift claw sequence (example)
        # move ZMotor or any lift mechanism here
        # XMotor/ZMotor movement if needed
        sleep(2)

        state = GAME_OVER

    # ---- GAME_OVER: reset game ----
    elif state == GAME_OVER:
        # move claw back home
        XMotor.stop()
        ZMotor.stop()
        calibration_sequence(XMotor,ZMotor,XLimSwitch, ZLimSwitch)
        ClawServo.write(0)
        sleep(1)
        state = IDLE

    # ---- small delay for loop ----
    sleep(0.01)  # prevents hogging CPU
    
        
  