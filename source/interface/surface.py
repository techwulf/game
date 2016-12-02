import pygame
import source.global_variables as global_variables

class Surface:
    surface = None

    resolution = (800, 600)
    flags = 0
    depth = 0

    def __init__(self, window):
        self.resolution = (window.width, window.height)

        self.surface = pygame.display.set_mode(
            self.resolution,
            0,
            32
        )

    def on_render(self):
        self.surface.fill(global_variables.BGCOLOR)

