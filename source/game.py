import pygame
from pygame.locals import *
import sys
from source.abstract.app import app
from interface import window
from source.environment.planet import planet

class Game(app.App):
    window          = None
    planet          = None

    def __init__(self):
        app.App.__init__(self)
        self.window = window.Window()
        self.planet = planet.Planet(self.window)
        pass

    def on_render(self):
        self.planet.on_render()
        self.post_render()
        pass

    def on_loop(self):
        while True:
            app.App.on_loop(self)
            self.planet.on_loop()
        pass
