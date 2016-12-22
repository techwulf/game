from source.global_variables import global_variables
from source.interface import keyboard
from source.interface import joystick
from source.abstract.entities.human import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        self.running()
        self.standing()
        self.on_axis_2()
        self.on_axis_3()
        self.on_key_up()
        self.on_key_right()
        self.on_key_down()
        self.on_key_left()
        self.on_key_return()

        self.translate()
        pass

    def running(self):
        if keyboard.KEYBOARD.L_SHIFT:
            self.run()
        else:
            self.walk()

    def standing(self):
        if keyboard.KEYBOARD.UP == False and joystick.JOYSTICK.AXIS_2 == 0:
            if keyboard.KEYBOARD.RIGHT == False and joystick.JOYSTICK.AXIS_3 == 0:
                if keyboard.KEYBOARD.DOWN == False and joystick.JOYSTICK.AXIS_2 == 0:
                    if keyboard.KEYBOARD.LEFT == False and joystick.JOYSTICK.AXIS_3 == 0:
                        self.stand()
        pass

    def on_axis_2(self):
        if joystick.JOYSTICK.AXIS_2 > joystick.JOYSTICK.dead_zone:
            self.direction = global_variables.EAST
            if joystick.JOYSTICK.AXIS_3 < -joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.NORTHEAST
            if joystick.JOYSTICK.AXIS_3 > joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.SOUTHEAST

        if joystick.JOYSTICK.AXIS_2 < -joystick.JOYSTICK.dead_zone:
            self.direction = global_variables.WEST
            if joystick.JOYSTICK.AXIS_3 < -joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.NORTHWEST
            if joystick.JOYSTICK.AXIS_3 > joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.SOUTHWEST
        pass

    def on_axis_3(self):
        if joystick.JOYSTICK.AXIS_3 < -joystick.JOYSTICK.dead_zone:
            self.direction = global_variables.NORTH
            if joystick.JOYSTICK.AXIS_2 > joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.NORTHEAST
            if joystick.JOYSTICK.AXIS_2 < -joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.NORTHWEST

        if joystick.JOYSTICK.AXIS_3 > joystick.JOYSTICK.dead_zone:
            self.direction = global_variables.SOUTH
            if joystick.JOYSTICK.AXIS_2 > joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.SOUTHEAST
            if joystick.JOYSTICK.AXIS_2 < -joystick.JOYSTICK.dead_zone:
                self.direction = global_variables.SOUTHWEST
        pass

    def on_key_up(self):
        if keyboard.KEYBOARD.UP == True:
            self.direction = global_variables.NORTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.NORTHEAST
            if keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.NORTHWEST
        pass

    def on_key_right(self):
        if keyboard.KEYBOARD.RIGHT == True:
            self.direction = global_variables.EAST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHEAST
            if keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHWEST
        pass

    def on_key_down(self):
        if keyboard.KEYBOARD.DOWN == True:
            self.direction = global_variables.SOUTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.SOUTHEAST
            if keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.SOUTHWEST
        pass

    def on_key_left(self):
        if keyboard.KEYBOARD.LEFT == True:
            self.direction = global_variables.WEST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHWEST
            if keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHWEST
        pass

    def on_key_return(self):
        if keyboard.KEYBOARD.RETURN == True:
            self.holding = self.parent.rock

        if keyboard.KEYBOARD.RETURN == False:
            self.holding = None
        pass
