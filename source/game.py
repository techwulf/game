import pygame
from pygame.locals import *
import sys
from source.hectare import hectare
from interface import window, keyboard, instructions, surface

class Game:
    hectare = None
    window = None
    surface = None
    clock = None
    frames_per_second = 30
    instructions = None

    def __init__(self):
        pygame.init()
        self.window = window.Window()
        self.hectare = hectare.Hectare()
        self.instructions = instructions.Instructions(self.window)
        self.surface = surface.Surface(self.window)
        pygame.display.set_caption(self.window.caption)

        self.clock = pygame.time.Clock()
        pass

    def on_quit(self):
        pygame.quit()
        sys.exit()
        pass

    def on_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            keyboard.KEYBOARD.key_event(event)
        pass

    def on_render(self):
        self.surface.on_render()
        self.hectare.on_render(self.surface.surface, self.window)
        self.instructions.on_render(self.surface.surface)
        pygame.display.update()
        pass

    def on_loop(self):
        while True:
            if keyboard.KEYBOARD.ESCAPE == True:
                self.on_quit()
            self.hectare.on_loop()
            self.on_event()
            self.on_render()
            self.hectare.boundary_check(self.window)
            self.clock.tick(self.frames_per_second)
        pass
