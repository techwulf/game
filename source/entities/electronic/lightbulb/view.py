from source.abstract.entities.inanimate import view
from source.action import action

import model

from animation_config import on, off

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(off.off_data)
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        if self.parent.battery.charge >= 50:
            if self.use_state != model.UseState.ON:
                self.use_state = model.UseState.ON
                self.animation = action.Action(on.on_data)
        else:
            if self.use_state != model.UseState.OFF:
                self.use_state = model.UseState.OFF
                self.animation = action.Action(off.off_data)
        
        self.animation.on_render(self)
        pass

