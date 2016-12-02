from source import global_variables
from source.interface import keyboard
from source.entities.entity import entity_controller

class AvatarController(entity_controller.EntityController):
    def __init__(self):
        entity_controller.EntityController.__init__(self)
        pass

    def on_loop(self):
        if keyboard.KEYBOARD.L_SHIFT:
            self.run()
        else:
            self.walk()

        if keyboard.KEYBOARD.UP == False:
            if keyboard.KEYBOARD.RIGHT == False:
                if keyboard.KEYBOARD.DOWN == False:
                    if keyboard.KEYBOARD.LEFT == False:
                        self.stand()

        if keyboard.KEYBOARD.UP == True:
            self.direction = global_variables.NORTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.NORTHEAST
            elif keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.NORTHWEST
        
        if keyboard.KEYBOARD.RIGHT == True:
            self.direction = global_variables.EAST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHEAST
            elif keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHEAST
        
        if keyboard.KEYBOARD.DOWN == True:
            self.direction = global_variables.SOUTH
            if keyboard.KEYBOARD.RIGHT == True:
                self.direction = global_variables.SOUTHEAST
            elif keyboard.KEYBOARD.LEFT == True:
                self.direction = global_variables.SOUTHWEST
        
        if keyboard.KEYBOARD.LEFT == True:
            self.direction = global_variables.WEST
            if keyboard.KEYBOARD.UP == True:
                self.direction = global_variables.NORTHWEST
            elif keyboard.KEYBOARD.DOWN == True:
                self.direction = global_variables.SOUTHWEST

        self.translate()