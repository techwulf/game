import pygame
import math

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class EntityModel:
    position = None

    direction = 0

    velocity_base = 4
    max_velocity = velocity_base * 2

    move_state = MoveState.STAND

    def __init__(self):
        self.position = pygame.math.Vector3(300, 200, 0)
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

    def run(self):
        self.move_state = MoveState.RUN

    def walk(self):
        self.move_state = MoveState.WALK

    def stand(self):
        self.move_state = MoveState.STAND