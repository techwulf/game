import pygame

class Window:
    resolution = None
    caption = "Demo"

    def __init__(self):
        self.resolution = pygame.math.Vector3(800, 600, 0)
        pass
