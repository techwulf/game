import pygame
import source.global_variables as global_variables

class Instructions:
    surface = None
    rectangle = None
    path_to_fonts = "./resources/fonts/"
    font_family = "hack"
    font = "Hack-BoldItalic.ttf"
    size = 16

    def __init__(self, window):
        self.font = pygame.font.Font(
            self.path_to_fonts+'/'+self.font_family+'/'+self.font,
            self.size
        )
        pass

        self.surface = self.font.render(
            'Arrow keys to move. Hold shift to run.',
            True,
            global_variables.WHITE
        )
        self.rectangle = self.surface.get_rect()
        self.rectangle.bottomleft = (10, window.resolution.y - 10)
        pass

    def on_render(self, camera):
        camera.surface.blit(
            self.surface,
            self.rectangle
        )
        pass
