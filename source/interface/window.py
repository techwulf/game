import pygame

class Window:
    resolution = None
    caption = "Demo"

    def __init__(self):
        self.resolution = pygame.math.Vector3(800, 600, 0)
        pygame.display.set_caption(self.caption)
        pass
