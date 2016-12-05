from source.abstract.entity import entity_view, action

from animation_config import stand

import random

class TileView(entity_view.EntityView):
    r = 0
    g = 0
    b = 0

    def __init__(self):
        entity_view.EntityView.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 100
        self.width = 100
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        pass

    def on_render(self, camera):
        """
        import pygame
        pygame.draw.rect(
            camera.surface,
            (self.r, self.g, self.b),
            [
                self.position.x - camera.position.x,
                self.position.y - camera.position.y,
                self.width,
                self.height,
            ],
            2
        )
        """
        
        if self.velocity() == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(
                camera,
                self.direction,
                self.position - camera.position
            )
        
        pass

