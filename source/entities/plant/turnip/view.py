from source.abstract.entities.inanimate import view
from source.action import action

from animation_config import healthy_seed, healthy_sprout, healthy_ripe, healthy_picked
from animation_config import damaged_seed, damaged_sprout, damaged_ripe, damaged_picked

import model

from datetime import datetime

import random

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(healthy_seed.healthy_seed_data)
        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        if self.health_state == model.HealthState.HEALTHY:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    self.growth_state = model.GrowthState.SEED
                    self.animation = action.Action(healthy_seed.healthy_seed_data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    self.growth_state = model.GrowthState.SPROUT
                    self.animation = action.Action(healthy_sprout.healthy_sprout_data)
            elif self.created_delta() > 20:
                if self.growth_state != model.GrowthState.RIPE:
                    self.growth_state = model.GrowthState.RIPE
                    self.animation = action.Action(healthy_ripe.healthy_ripe_data)
        
        if self.health_state == model.HealthState.DAMAGED:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    self.growth_state = model.GrowthState.SEED
                    self.animation = action.Action(damaged_seed.damaged_seed_data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    self.growth_state = model.GrowthState.SPROUT
                    self.animation = action.Action(damaged_sprout.damaged_sprout_data)
            elif self.created_delta() > 20:
                if self.growth_state != model.GrowthState.RIPE:
                    self.growth_state = model.GrowthState.RIPE
                    self.animation = action.Action(damaged_ripe.damaged_ripe_data)
        
        self.animation.on_render(self)
        pass

