import pygame

class AvatarModel:
    position = pygame.math.Vector3(300, 200, 0)

    direction = 0
    velocity_base = 4
    velocity_modifier = 0
    max_velocity = velocity_base * 2

    def __init__(self):
        pass

    def velocity(self):
        return self.velocity_base * self.velocity_modifier