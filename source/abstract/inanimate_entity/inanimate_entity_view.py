import pygame

from source.abstract.entity import entity_view, action

from animation_config import stand

class InanimateEntityView(entity_view.EntityView):
    def __init__(self):
        entity_view.EntityView.__init__(self)

        self.height = 32
        self.width = 32
        pass

    def on_render(self, camera):
        pass
