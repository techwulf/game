import pygame
import math

from source.abstract.entities.animate import model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class Model(model.Model):
    holding = None
    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass

    def run(self):
        self.move_state = MoveState.RUN
        pass

    def walk(self):
        self.move_state = MoveState.WALK
        if self.holding != None:
            self.holding.position.x = self.position.x
            self.holding.position.y = self.position.y
        pass
