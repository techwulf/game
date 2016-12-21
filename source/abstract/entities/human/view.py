from source.action import action
from source.abstract.entities.animate import view
from source.abstract.entities.human.model import MoveState

from animation_config import run
from animation_config import stand
from animation_config import walk

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.height = 74
        self.width = 32
        pass

    def on_render(self):
        if self.move_state == MoveState.STAND:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(self)
        elif self.move_state == MoveState.WALK:
            if self.animation == None or self.animation.action != "walk":
                self.animation = action.Action(walk.walk_data)
            self.animation.on_render(self)
        elif self.move_state == MoveState.RUN:
            if self.animation == None or self.animation.action != "run":
                self.animation = action.Action(run.run_data)
            self.animation.on_render(self)
        else:
            print("Human.on_render() invalid option.")
        pass
