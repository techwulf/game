import pygame
import source.global_variables as global_variables

class Camera:
    surface    = None
    position   = None
    center     = None
    resolution = None
    flags      = 0
    depth      = 0

    def __init__(self, window):
        self.position   = pygame.math.Vector3(0, 0, 0)
        self.resolution = pygame.math.Vector3(window.resolution.x, window.resolution.y, 0)
        self.center     = pygame.math.Vector3(self.resolution.x / 2, self.resolution.y / 2, 0)

        self.surface = pygame.display.set_mode(
            (int(self.resolution.x), int(self.resolution.y)),
            0,
            32
        )
        pass

    def set_target(self, target):
        self.position = target.position
        pass

    def on_render(self):
        self.surface.fill(global_variables.BGCOLOR)
        pass

    def in_viewport(self, obj):
        x = (self.position.x) - obj.width
        y = (self.position.y) - obj.height
        w = (self.position.x + self.resolution.x)
        h = (self.position.y + self.resolution.y)

        if obj.position.x > x and obj.position.x < w:
            if obj.position.y > y and obj.position.y < h:
                return True
        obj.animation = None
        return False
        pass
