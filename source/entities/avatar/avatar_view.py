from source.entities.entity import entity_view

from source.entities.entity import action

from animation_config import run
from animation_config import stand
from animation_config import walk

class AvatarView(entity_view.EntityView):
    walk_action = None
    run_action = None

    def __init__(self):
        entity_view.EntityView.__init__(self)

        self.walk_action = action.Action(walk.walk_data)
        self.run_action = action.Action(run.run_data)

        self.height = 74
        self.width = 32
        pass

    def on_render(self, surface, window):
        if self.velocity() == 0:
            self.stand_action.render(surface, self.direction, self.position)
        elif self.velocity() <= self.velocity_base:
            self.walk_action.render(surface, self.direction, self.position)
        elif self.velocity() <= self.max_velocity:
            self.run_action.render(surface, self.direction, self.position)
        else:
            print("Entity.on_render() invalid option.")
        pass
