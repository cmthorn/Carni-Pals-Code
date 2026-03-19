from machine import Pin,PWM, ADC


class limit_switch:
    def __init__(self,num):
        self.LS = Pin(num, Pin.IN, Pin.PULL_UP)
    def pressed(self) -> bool:
        # if self.LS.value() == 1:
        return self.LS.value() == 1

    def test(self):
        return(self.LS.value())


class Button: 
    def __init__(self,pin_num):
        self.button = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    def pressed(self):
        return self.button.value()


class Joystick: 
    def __init__(self, Vy, Vx):
        self.x_axis = ADC(Pin(Vx))  # X-axis
        self.y_axis = ADC(Pin(Vy))  # Y-axis

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def on(self):
        x_val = self.x_axis.read_u16()
        y_val = self.y_axis.read_u16()

        x_mapped = self.map(x_val, 200,65535, -100,100)
        y_mapped = self.map(y_val, 200,65535, -100,100)

        return [x_mapped, y_mapped]

    def drift_fix(self,x,y):
        new_x = x
        new_y = y

        if -1<x<1: 
            new_x= 0
        if -1<y<1: 
            new_y= 0

        return [new_x,new_y]


        