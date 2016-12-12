import pygame
import math

from source.abstract.entities.entity import model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class Model(model.Model):
    velocity_base = 4
    max_velocity = velocity_base * 2

    vision = 800
    resolution = None

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        self.resolution = pygame.math.Vector3(self.vision, self.vision, 0)
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
