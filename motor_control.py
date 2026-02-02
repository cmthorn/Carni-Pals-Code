import math
import time

class Motor:
    def __init__(self, pin_num):
        self.pin = pin_num


class Servo(Motor):
    def __init__(self, pin_num):
        super().__init__(pin_num)
        self.ServoPulseLen = None # only applicable to servos 


    def ServoSpin(self, servo, desired_position) -> None:
        """
        Docstring for ServoSpin
        :param desired_position: The Desired Position (in degrees)
        :param servo: the servo object we want to spin 

        This function takes in the desired position for a servo to spin to.
        It will convert degrees to pulse length, and set the servo to the position.

        """

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
    def __init__(self, RPWM,LPWM):
        #FOR BTS7960 Driver Logic
        self.LPWM = LPWM
        self.RPWM = RPWM

        #For Quadtrature Encoders
    
    def DCSpinCW(self, length,r):
        """
        Docstring for DCSpinCW
        
        :param self: Description
        :param length: Description
        """
        roation = self.ConvertDistToRotation(length, r)
    
    def DCSpinCCW(self, length,r):
        """
        Docstring for DCSpinCW
        
        :param self: Description
        :param length: Description
        """
        roation = -self.ConvertDistToRotation(length, r)

    

    def ConvertDistToRotation(self,length,r) -> float: 
        """
        Docstring for ConvertDistToRotation
       
        :param length: The desired lenght to travel 
        :return: the amount of rotations Neccecary 
        :rtype: float
        """
        Circumference =float( 2 * (3.14159) * r)
        return length/Circumference