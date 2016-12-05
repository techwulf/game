import pygame

from source.abstract.entity import entity_view, action

from animation_config import run
from animation_config import stand
from animation_config import walk

class AnimateEntityView(entity_view.EntityView):
    def __init__(self):
        entity_view.EntityView.__init__(self)

        self.height = 32
        self.width = 32
        pass

    def on_render(self, camera):
        pass
