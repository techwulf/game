import pygame
import source.pyganim.pyganim as pyganim
import source.global_variables as global_variables
import animation
import action

import animation_config.run as run
import animation_config.stand as stand
import animation_config.walk as walk

class AvatarView:
    height = None
    width = None

    stand_action = action.Action(stand.stand_data)
    walk_action = action.Action(walk.walk_data)
    run_action = action.Action(run.run_data)

    def __init__(self):
        self.height = 70
        self.width = 32

    def on_render(self, surface, window):
        if self.velocity() == 0:
            self.stand_action.render(surface, self.direction, self.position)
        elif self.velocity() <= self.velocity_base:
            self.walk_action.render(surface, self.direction, self.position)
        elif self.velocity() <= self.max_velocity:
            self.run_action.render(surface, self.direction, self.position)
        else:
            print("Avatar.on_render() invalid option.")
