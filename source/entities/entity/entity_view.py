import action

from animation_config import run
from animation_config import stand
from animation_config import walk

class EntityView:
    height = None
    width = None

    stand_action = action.Action(stand.stand_data)
    walk_action = action.Action(walk.walk_data)
    run_action = action.Action(run.run_data)

    def __init__(self):
        self.height = 70
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