import pygame
from pygame.locals import *
import sys
from source.abstract.app import app
from source.hectare import hectare
from interface import window, keyboard, instructions, camera

class Game(app.App):
    camera              = None
    hectare             = None
    window              = None
    instructions        = None

    def __init__(self):
        app.App.__init__(self)
        self.window = window.Window()
        self.hectare = hectare.Hectare()
        self.instructions = instructions.Instructions(self.window)
        self.camera = camera.Camera(self.window)
        self.camera.set_target(self.hectare.avatar)
        pass

    def on_render(self):
        self.camera.fill_surface()
        self.hectare.on_render(self.camera)
        self.instructions.on_render(self.camera)
        self.post_render()
        pass

    def on_loop(self):
        while True:
            app.App.on_loop(self)
            self.hectare.on_loop()
        pass
