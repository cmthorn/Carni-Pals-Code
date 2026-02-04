from output_control import Servo, DC, Stepper, Electromagnet
from machine import Pin

class Gantry_SYS:
    def __init__(self, XDC: DC, YDC:DC):
        self.XMotor = XDC
        self.YMotor = YDC



class Claw_SYS:
    def __init__(self, 
        servo: Servo, 
        EM: Electromagnet, 
        Stepper: Stepper, 
        Switcher:Stepper,
        limitSwitch, # specifiy this as a limit switch object later on
        start:str

        ):

        """
        INITIALIZE CLAW CLASS-> Sets up the claw with the 3 types of claws available
        Params: Motor Types, start -> ["Reg","EMag","Scoop"] 
        """

        self.Swicher = Switcher
        self.Cservo = servo #for regular claw
        self.CEmag = EM # electromagnet claw
        self.CStep = Stepper # for the scooper
        self.LS = limitSwitch
        self.claws = {"Reg":self.Cservo, "EMag":self.CEmag, "Scoop":self.CStep} # claw map
        self.positions = [-120,0,120]
        self.current_claw = self.claws[start] # sets the current claw to the starting claw type

    def HomeBasePos(self):
        
        """
        In a while loop increase change factor slowly and spin the switcher motor CW and CCW 
        until the limit switch is pressed, then stop the Stepper in that position.
        """

        ChangeFactor = 1


    def SetClaw(self,desired_claw:str):
        """
        Sets Game claw to desired Claw. [USE STATES]

        1. Home the Claw somehow 
        2. Check current claw and desired claw
        3. Figure out which way to move to get to desired state 
        4. Spin switcher motor in the correct direction and duration 
        5. Check if Limit switch has been pressed just in case, If it has Stop and correct 
        . make the current claw the desired claw 
        
       
        
        """
        =
    
        self.current_claw = self.claws[desired_claw]

    def RegOpen(self):
        pass
    def RegClose(self):
        pass

    def ScoopUp(self):
        pass

    def ScoopDown(self):
        pass

    def EMagOn(self):
        pass

    def EMagOff(self):
        pass

    def clawSequence(self):
        pass