import pygame
from pygame.locals import *
import sys
from entities.avatar import avatar
from entities.tile import tile
from interface import window, keyboard, instructions, surface

class Game:
    entities = None
    window = None
    surface = None
    clock = None
    frames_per_second = 30
    instructions = None

    def __init__(self):
        pygame.init()
        self.window = window.Window()
        self.entities = [
            avatar.Avatar(),
            tile.Tile()
        ]
        self.instructions = instructions.Instructions(self.window)
        self.surface = surface.Surface(self.window)
        pygame.display.set_caption(self.window.caption)

        self.clock = pygame.time.Clock()

    def on_quit(self):
        pygame.quit()
        sys.exit()

    def on_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.on_quit()
            keyboard.KEYBOARD.key_event(event)

    def on_render(self):
        self.surface.on_render()
        for entity in self.entities:
            entity.on_render(
                self.surface.surface,
                self.window
            )
        self.instructions.on_render(self.surface.surface)
        pygame.display.update()

    def on_loop(self):
        while True:
            if keyboard.KEYBOARD.ESCAPE == True:
                self.on_quit()
            for entity in self.entities:
                entity.on_loop()
            self.on_event()
            self.on_render()
            self.boundary_check()
            self.clock.tick(self.frames_per_second)

    def boundary_check(self):
        for entity in self.entities:
            if entity.position.x < 0:
                entity.position.x = 0
            if entity.position.x > self.window.width - entity.width:
                entity.position.x = self.window.width - entity.width
            if entity.position.y < 0:
                entity.position.y = 0
            if entity.position.y > self.window.height - entity.height:
                entity.position.y = self.window.height - entity.height
