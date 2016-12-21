import pygame
from source.global_variables import global_variables

class Window:
    resolution = None
    caption = "Demo"

    def __init__(self):
        self.resolution = pygame.math.Vector3(global_variables.RESOLUTION_X, global_variables.RESOLUTION_Y, 0)
        pygame.display.set_caption(self.caption)
        pass
