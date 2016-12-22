import pygame

from source.abstract.entities.entity import model
from source.global_variables import global_variables

class MoveState():
    STAND   = 0
    WALK    = 1
    RUN     = 2

class Model(model.Model):
    walk_speed  = 4
    run_speed   = 4
    velocity    = None

    is_walking  = 0
    is_running  = 0

    vision      = 800
    resolution  = None

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        self.resolution = pygame.math.Vector3(self.vision, self.vision, 0)
        self.velocity = pygame.math.Vector3()
        pass
    
    def translate(self):
        self.position.x += self.velocity.x * ((self.walk_speed) + (self.is_running * self.run_speed))
        self.position.y += self.velocity.y * ((self.walk_speed) + (self.is_running * self.run_speed))
        pass

    def set_animation(self):
        if self.velocity.length() == 0:
            self.stand()
        if self.velocity.length() > abs(0):
            self.walk()
        if self.velocity.length() > abs(4):
            self.run()

    def set_direction(self):
        if self.velocity.y < 0:
            self.direction = global_variables.NORTH
        if self.velocity.x > 0:
            self.direction = global_variables.EAST
        if self.velocity.y > 0:
            self.direction = global_variables.SOUTH
        if self.velocity.x < 0:
            self.direction = global_variables.WEST
        pass

    def move_x(self, value):
        self.velocity.x = value
        pass

    def move_y(self, value):
        self.velocity.y = value
        pass

    def start_running(self):
        self.is_running = 1

    def stop_running(self):
        self.is_running = 0

    def stop(self):
        self.velocity   = pygame.math.Vector3(0, 0, 0)
        self.is_walking = 0
        self.is_running = 0
        pass
