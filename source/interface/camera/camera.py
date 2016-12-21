import pygame
from source.global_variables import global_variables

class Camera:
    surface    = None
    position   = None
    center     = None
    resolution = None
    flags      = 0
    depth      = 32

    def __init__(self):
        self.position   = pygame.math.Vector3(0, 0, 0)
        self.resolution = pygame.math.Vector3(global_variables.RESOLUTION_X, global_variables.RESOLUTION_Y, 0)
        self.center     = pygame.math.Vector3(self.resolution.x / 2, self.resolution.y / 2, 0)

        self.surface = pygame.display.set_mode(
            (int(self.resolution.x), int(self.resolution.y)),
            self.flags,
            self.depth
        )
        pass

    def set_target(self, target):
        self.position = target.position
        pass

    def fill_surface(self):
        self.surface.fill(global_variables.BGCOLOR)
        pass

    def render_animation(self, obj, obj_position):
        obj.blit(
            self.surface,
            (
                obj_position.x - self.position.x + (self.resolution.x / 2),
                obj_position.y - self.position.y + (self.resolution.y / 2)
            )
        )
        pass

    def render_frame(self, obj, obj_position):
        self.surface.blit(
            obj,
            (
                obj_position.x - self.position.x + (self.resolution.x / 2),
                obj_position.y - self.position.y + (self.resolution.y / 2)
            )
        )
        pass

    def in_viewport(self, obj):
        x = self.position.x - (self.resolution.x / 2)
        y = self.position.y - (self.resolution.y / 2)
        w = self.position.x + (self.resolution.y / 2)
        h = self.position.y + (self.resolution.y / 2)

        if obj.position.x > x or obj.position.x < w:
            if obj.position.y > y or obj.position.y < h:
                return True
        obj.animation = None
        return False
        pass
