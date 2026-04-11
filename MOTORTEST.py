from machine import Pin, PWM
import time
import config

ina1 = Pin(9,Pin.OUT)
ina2 = Pin(10, Pin.OUT)
pwma = PWM(Pin(11))

pwma.freq(1000)
speed_percent = 50
sleep_time = 1
led = Pin(0, Pin.OUT)



def RotateCW(duty):
    ina1.value(1)
    ina2.value(0)
    duty_16 = int((duty*65536)/100)
    pwma.duty_u16(duty_16)
   
def StopMotor():
    ina1.value(0)
    ina2.value(0)
    pwma.duty_u16(0)

RotateCW(speed_percent)
while True:
    led.on()
    