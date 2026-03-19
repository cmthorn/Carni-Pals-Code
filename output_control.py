from machine import Pin,PWM
from time import sleep
import neopixel


class Servo:
    def __init__(self, pin, min_us=600, max_us=2600, freq=50):
        self.min_us = min_us
        self.max_us = max_us
        self.period_us = 1000000 // freq  # 20,000 us for 50Hz

        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)


    def write(self, angle):
        """
        Set servo angle (0–180 degrees)
        """
        # Clamp angle so you don't destroy your servo
        angle = max(0, min(180, angle))

        # Convert angle → pulse width
        pulse_us = self.min_us + (self.max_us - self.min_us) * angle / 180

        # Convert pulse width → 16-bit duty cycle
        duty = int((pulse_us / self.period_us) * 65535)

        self.pwm.duty_u16(duty)

    def deinit(self):
        """
        Turn off PWM (optional cleanup)
        """
        self.pwm.deinit()

class Electromagnet:
    def __init__(self, pin_num):
        self.EM = Pin(pin_num, Pin.OUT)

    def ElectromagnetOn(self):
        """
        Docstring for ElectromagnetOn
        
        :param self: Description
        """
        self.EM.on()

    def ElectromagnetOff(self):
        """
        Docstring for ElectromagnetOff
        
        :param self: Description
        """
        self.EM.off()

class Stepper:
    def __init__(self, pin_num):
        """
        Docstring for init 
        """
     
        self.pins = [pin_num + i for i in range(4)]

        self.step_sequence = [
            [1,0,0,1],
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1]
        ]
    def StepperSpin(self, steps=512, delay=0.002, clockwise =True):
        """
        Docstring for StepperSpin
        
        :param self: Description
        """
        if clockwise:
            seq = self.step_sequence
        else:
            seq = list(reversed(self.step_sequence))

        for i in range(steps):
            for step in seq:
                which_pins = {pin: val for pin, val in zip(self.pins, step)}
                print(which_pins)
                time.sleep(delay)
        


class DC:
    def __init__(
            self,
            RPWM,
            LPWM,
            freq = 20000,
            encA = None, # defualt as none
            encB = None
            ):
        #FOR BTS7960 Driver pin setup 
        self.LPWM = PWM(Pin(LPWM))
        self.RPWM = PWM(Pin(RPWM))
        #Def PWM FreqS
        self.LPWM.freq(freq)
        self.RPWM.freq(freq)

        #Optional Quadrature Encoder Pin setup 
        self.encA = Pin(encA, Pin.IN,Pin.PULL_UP) if encA is not None else None
        self.encB = Pin(encB, Pin.IN,Pin.PULL_UP) if encB is not None else None

        self.position = 0 # to keep track of the current position.
    
    def stop(self):
        self.RPWM.duty_u16(0)
        self.LPWM.duty_u16(0)

    def set_speed(self, speed):
        """
        speed: -100 to 100
        positive = forward
        negative = backward
        """
        speed = max(-100, min(100, speed)) #makes sure speed is in between -100 and 100 
        duty = int(abs(speed) / 100 * 65535) 
        
        if speed > 0:
            self.RPWM.duty_u16(duty)
            self.LPWM.duty_u16(0)
        elif speed < 0:
            self.RPWM.duty_u16(0)
            self.LPWM.duty_u16(duty)
        else:
            # print("Jarvis? Jork it")
            self.stop()
    
class led_strip:
    def __init__(self, num_lights, num_pin):
        self.n = num_lights
        self.p = num_pin

        self.np = neopixel.NeoPixel(Pin(self.p),self.n)

    def party_time(self):
        self.np[0] = (255,0,0)
        self.np[1] = (255,165,0)
        self.np[2] = (255,255,0)
        self.np[3] = (0,255,25)
        self.np[4] = (0,0,255)
        self.np[5] = (128,0,128)
        self.np[6] = (255,0,255)
        self.np[7] = (255,255,255)
        self.np[8] = (255,0,0)
        self.np[9] = (0,255,255)
        self.np[10] = (0,0,255)
        self.np[11] = (0,255,0)
        self.np.write()
        sleep(2)
        for i in range(self.n):
            self.np[i] = (0,0,0)
        self.np.write()



  
    