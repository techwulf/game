import pygame
from pygame.locals import *
import sys

from source.interface import keyboard

class App:
    clock               = None
    frames_per_second   = 30

    def __init__(self):
        pygame.init()
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

    def on_loop(self):
        if keyboard.KEYBOARD.ESCAPE == True:
            self.on_quit()
        self.on_event()
        self.on_render()
        self.clock.tick(self.frames_per_second)
        pass

    def post_render(self):
        pygame.display.update()
        pygame.display.flip()
        pass
