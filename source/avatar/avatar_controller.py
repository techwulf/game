import math
import pygame
from pygame.locals import *
import source.global_variables as global_variables
import source.interface.keyboard as keyboard

class AvatarController:
    def __init__(self):
        pass

    def move(self):
        if keyboard.KEYBOARD.L_SHIFT:
            self.run()
        else:
            self.walk()

        if keyboard.KEYBOARD.UP == False and keyboard.KEYBOARD.RIGHT == False and keyboard.KEYBOARD.DOWN == False and keyboard.KEYBOARD.LEFT == False:
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
        
        self.position.x = (
            self.position.x + self.velocity() * math.sin(math.radians(self.direction))
        )
        self.position.y = (
            self.position.y + -self.velocity() * math.cos(math.radians(self.direction))
        )

    def run(self):
        self.velocity_modifier = 2

    def walk(self):
        self.velocity_modifier = 1

    def stand(self):
        self.velocity_modifier = 0

    def on_loop(self):
        self.move()