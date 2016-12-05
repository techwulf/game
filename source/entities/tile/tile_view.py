from source.abstract.inanimate_entity import inanimate_entity_view
from source.action import action

from animation_config import stand

import random

class TileView(inanimate_entity_view.InanimateEntityView):
    def __init__(self):
        inanimate_entity_view.InanimateEntityView.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 100
        self.width = 100
        pass

    def on_render(self, camera):
        if self.animation == None or self.animation.action != "stand":
            self.animation = action.Action(stand.stand_data)
        self.animation.on_render(
            camera,
            self.direction,
            self.position - camera.position
        )
        
        pass

