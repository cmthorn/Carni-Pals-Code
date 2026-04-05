from machine import Pin,PWM, UART
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
        Turn off PWM 
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
    def __init__(self, p1,p2,p3,p4,delay = 0.005):
        """
        Docstring for init 
        """
     
        self.pins = [
            Pin(p1,Pin.OUT),
            Pin(p2,Pin.OUT),
            Pin(p3,Pin.OUT),
            Pin(p4,Pin.OUT)
        ]
        self.delay = delay

        self.step_sequence = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ]
    def step(self, cycles, direction=1):
        
        sequence = self.step_sequence if direction == 1 else self.step_sequence[::-1]
    
        for s in range(cycles):
            for step in sequence:
                for i in range(4):
                    self.pins[i].value(step[i])
                sleep(self.delay)

    def stop(self):
        for pin in self.pins:
            pin.value(0)
        


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


class Speaker():
    def __init__(self, busy_pin, Tx=0, Rx=1, main_theme =3, grab_music =2,sucess =3, fail = 4):
        self.uart = UART(0, baudrate=9600, tx=Tx, rx=Rx)
        self.busy = Pin(busy_pin, Pin.IN)  # DFPlayer BUSY pin
        self.main_theme = main_theme
        self.grab_music = grab_music
        self.sucess = sucess
        self.fail = fail 
    
    def is_busy(self) ->bool:
        return self.busy.value() == 1

    def bgMusic(self):
        self.uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,self.main_theme,0xEF]))

    def grabMusic(self):
        self.uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,self.grab_music,0xEF]))

    def sucessMusic(self):
        self.uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,self.sucess,0xEF]))

    def failMusic(self):
        self.uart.write(bytearray([0x7E,0xFF,0x06,0x03,0x00,0x00,self.fail,0xEF]))

    def stop(self):
        self.uart.write(bytearray([0x7E,0xFF,0x06,0x16,0x00,0x00,0x00,0xEF]))