import pygame
import source.global_variables as global_variables

class Instructions:
    surface = None
    rectangle = None
    path_to_fonts = "./resources/fonts/"
    font_family = "hack"
    font = "Hack-BoldItalic.ttf"

    def __init__(self, window):
        self.font = pygame.font.Font(self.path_to_fonts+'/'+self.font_family+'/'+self.font, 16)

        self.surface = self.font.render(
            'Arrow keys to move. Hold shift to run.',
            True,
            global_variables.WHITE
        )
        self.rectangle = self.surface.get_rect()
        self.rectangle.bottomleft = (10, window.height - 10)

    def on_render(self, surface):
        surface.blit(
            self.surface,
            self.rectangle
        )