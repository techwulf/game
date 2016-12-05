import pygame
import math

from source.abstract.entity import entity_model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class AnimateEntityModel(entity_model.EntityModel):
    velocity_base = 4
    max_velocity = velocity_base * 2

    def __init__(self):
        entity_model.EntityModel.__init__(self)
        pass
    
    def velocity(self):
        return self.velocity_base * self.move_state

    def translate(self):
        self.position.x = (
            self.position.x + self.velocity() * math.sin(
                math.radians(self.direction)
            )
        )
        self.position.y = (
            self.position.y + -self.velocity() * math.cos(
                math.radians(self.direction)
            )
        )
