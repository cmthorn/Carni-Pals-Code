from machine import Pin,PWM

class input_handler:
    def __init__(self):
        # populate w/sensors
        self.tasks = {}

    def update_tasks(self) -> dict{str:object}:
        # check all sensors pressed
        return self.tasks