import pygame
import math

from source.abstract.entities.entity import model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class Model(model.Model):
    walk_speed = 4
    run_speed = walk_speed * 2

    vision = 800
    resolution = None

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        self.resolution = pygame.math.Vector3(self.vision, self.vision, 0)
        pass

    def velocity(self):
        if self.move_state == MoveState.STAND:
            return 0
        elif self.move_state == MoveState.WALK:
            return self.walk_speed
        elif self.move_state == MoveState.RUN:
            return self.run_speed
        else:
            print("Animate.move_state invalid option.")

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
