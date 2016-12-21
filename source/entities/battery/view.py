from source.abstract.entities.inanimate import view
from source.action import action

import model

from animation_config import percent_000, percent_020, percent_040, percent_060, percent_080, percent_100

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(percent_000.percent_000_data)
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        if self.charge < 19:
            if self.charge_state != model.ChargeState.PERCENT_000:
                self.charge_state = model.ChargeState.PERCENT_000
                self.animation = action.Action(percent_000.percent_000_data)
        if self.charge >= 20 and self.charge <= 39:
            if self.charge_state != model.ChargeState.PERCENT_020:
                self.charge_state = model.ChargeState.PERCENT_020
                self.animation = action.Action(percent_020.percent_020_data)
        if self.charge >= 40 and self.charge <= 59:
            if self.charge_state != model.ChargeState.PERCENT_040:
                self.charge_state = model.ChargeState.PERCENT_040
                self.animation = action.Action(percent_040.percent_040_data)
        if self.charge >= 60 and self.charge <= 79:
            if self.charge_state != model.ChargeState.PERCENT_060:
                self.charge_state = model.ChargeState.PERCENT_060
                self.animation = action.Action(percent_060.percent_060_data)
        if self.charge >= 80 and self.charge <= 99:
            if self.charge_state != model.ChargeState.PERCENT_080:
                self.charge_state = model.ChargeState.PERCENT_080
                self.animation = action.Action(percent_080.percent_080_data)
        if self.charge >= 100:
            if self.charge_state != model.ChargeState.PERCENT_100:
                self.charge_state = model.ChargeState.PERCENT_100
                self.animation = action.Action(percent_100.percent_100_data)
        
        self.animation.on_render(self)
        pass

