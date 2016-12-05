from source.action import action

from animation_config import stand

class EntityView:
    height = None
    width  = None

    animation = None

    def __init__(self):
        self.height = 32
        self.width = 32
        pass

    def on_render(self, camera):
        if self.velocity() == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(
                camera,
                self.direction,
                self.position - camera.position
            )
        pass
