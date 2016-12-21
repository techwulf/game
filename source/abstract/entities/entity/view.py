from source.action import action

from animation_config import stand
from source.global_variables.camera import CAMERA

class View:
    height = None
    width  = None

    animation = None

    def __init__(self):
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        if self.velocity() == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(
                self.direction,
                self.position - CAMERA.position
            )
        pass
