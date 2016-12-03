import action

from animation_config import run
from animation_config import stand
from animation_config import walk

class EntityView:
    height = None
    width = None

    stand_action = None

    def __init__(self):
        self.stand_action = action.Action(stand.stand_data)
        
        self.height = 32
        self.width = 32
        pass

    def on_render(self, surface, window):
        if self.velocity() == 0:
            self.stand_action.render(surface, self.direction, self.position)
        pass
