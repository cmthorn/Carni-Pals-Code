
class motors():
    def __init_(self, pin_num,type):
        self.pin= pin_num
        self.type = type # Valid types: Stepper, DC, Servo 

    def ServoSpin(self,desired_position) -> None:
        """
        Docstring for ServoSpin
        :param desired_position: The Desired Position (in degrees)

        This functino takes in the desired position for a servo to spin to.
        It will convert degrees to 

        """
