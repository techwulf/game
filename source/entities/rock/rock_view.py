from source.abstract.inanimate_entity import inanimate_entity_view
from source.abstract.entity import action

from animation_config import stand

import random

class RockView(inanimate_entity_view.InanimateEntityView):
    def __init__(self):
        inanimate_entity_view.InanimateEntityView.__init__(self)
        self.animation = action.Action(stand.stand_data)
        self.height = 32
        self.width = 32
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

