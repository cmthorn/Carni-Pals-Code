from machine import Pin,PWM


class limit_switch:
    def __init__(self,num):
        self.LS = Pin(num, Pin.IN, Pin.PULL_UP)
    def pressed(self) -> bool:
        # if self.LS.value() == 1:
        return self.LS.value() == 1

    def test(self):
        return(self.LS.value())