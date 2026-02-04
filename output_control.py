from machine import Pin,PWM


class Motor:
    def __init__(self, pin_num):
        self.pin = pin_num


class Servo(Motor):
    def __init__(self, pin_num):
        super().__init__(pin_num)
        self.ServoPulseLen = None # only applicable to servos 


    def ServoSpin(self, desired_position) -> None:
        """
        Docstring for ServoSpin
        :param desired_position: The Desired Position (in degrees)
        :param servo: the servo object we want to spin 

        This function takes in the desired position for a servo to spin to.
        It will convert degrees to pulse length, and set the servo to the position.

        """

class Electromagnet(Motor):
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

class Stepper(Motor):
    def __init__(self, pin_num):
        """
        Docstring for init 
        """
        super().__init__(pin_num)
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
        


class DC():
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
            self.stop()


  
    