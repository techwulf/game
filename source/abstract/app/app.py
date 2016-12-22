import pygame
from pygame.locals import *
import sys

from source.interface import keyboard
from source.interface import joystick

class App:
    clock               = None
    frames_per_second   = 30

    universe = None

    def __init__(self):
        pygame.init()
        keyboard.KEY_ESCAPE.subscribe(self)
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
            joystick.JOYSTICK.joystick_event(event)
        pass

    def on_keydown_escape(self):
        pass

    def on_keyup_escape(self):
        self.on_quit()

    def on_render(self):
        self.universe.on_render()
        self.post_render()
        pass

    def on_loop(self):
        while True:
            self.on_event()
            self.on_render()
            self.clock.tick(self.frames_per_second)
            self.universe.on_loop()
        pass

    def post_render(self):
        pygame.display.update()
        pygame.display.flip()
        pass
