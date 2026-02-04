from output_control import Servo,DC,Stepper
from machine import Pin


class Claw:
    def __init__(self, servo: Servo, ):
        self.servo = servo
