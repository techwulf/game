import pygame

from source.action import action
from source.abstract.entities.entity import view

from animation_config import run
from animation_config import stand
from animation_config import walk

class View(view.View):
    def __init__(self):
        view.View.__init__(self)

        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        pass
