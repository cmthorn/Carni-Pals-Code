
from output_control import Servo, DC, Stepper, Electromagnet
from machine import Pin


class Controller: 
    def __init__(self, GantryX, GantryY, LimSwitch1, LimSwitch2):
        self.PossibleStates = ["Idling","Player_Control", "Lowering", "Grab"]
        self.state = self.PossibleStates[0]
        self.GantryY = GantryY
        self.GantryX = GantryX
        self.LimSwitch1 = LimSwitch1
        self.LimSwitch2 = LimSwitch2
      
    
    def update(self):
        if self.state == "Idling": 
            #set everything to 0
            self.GantryX.set_speed(0)
            self.GantryY.set_speed(0)

            #check if any events occur and set the state to Player Control
            if self.LimSwitch1.pressed():
                self.state = self.PossibleStates[1]
            if self.LimSwitch2.pressed():
                self.state = self.PossibleStates[1]
        
        if self.state == "Player_Control":
            if self.LimSwitch1.pressed():
                self.GantryX.set_speed(100)
                self.GantryY.set_speed(100)
            elif self.LimSwitch2.pressed():
                self.GantryX.set_speed(-100)
                self.GantryY.set_speed(-100)
            else:
                self.state = self.PossibleStates[0]
            
            

class State:
    def __init__(self):
        self.active = False

    def start(self):
        self.active = True

    def stop(self):
        self.active = False

    def update(self):
        pass

class DCMotorState(State):
    def __init__(self, motor: DC):
        super().__init__()
        self.motor = motor

    def StartCW(self):
        super().start()
        self.motor.set_speed(100)
    
    def StartCCW(self):
        super().start()
        self.motor.set_speed(-100)

    def Stop(self):
        super().stop()
        self.motor.set_speed(0)
        


