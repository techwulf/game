import pygame
from libs.pyganim import pyganim
from source.global_variables.camera import CAMERA

class Animation:
    entity_name         = None
    path_to_images      = "resources/images/"
    action              = None
    direction           = None
    animation_object    = None
    directory           = None
    move_conductor      = None

    def __init__(self, data, animation):
        self.entity_name    = data["entity_name"]
        self.action         = data["action"]
        self.direction      = animation["direction"]
        self.load_frames(animation["frames"])
        pass
    
    def path_to_animations(self):
        return self.path_to_images+self.entity_name+"/animations/"

    def load_frames(self, f):
        if len(f) > 1:
            self.load_animation(f)
        else:
            self.load_frame(f)
        pass

    def load_animation(self, f):
        frames = []
        for fr in f:
            tmp_frame = self.path_to_animations()+self.action+'/'+self.direction+'/'+fr[0]
            tmp_duration = fr[1]
            fra = (tmp_frame, tmp_duration)
            frames.append(fra)
            self.animation_object = pyganim.PygAnimation(frames)
            self.move_conductor = pyganim.PygConductor(self.animation_object)

    def load_frame(self, f):
        tmp_frame = self.path_to_animations()+self.action+'/'+self.direction+'/'+f[0][0]
        fra = pygame.image.load(tmp_frame).convert_alpha()
        self.animation_object = fra

    def on_render(self, obj):
        if isinstance(self.animation_object, pyganim.PygAnimation):
            self.move_conductor.play()
            CAMERA.render_animation(self.animation_object, obj.position)
        else:
            CAMERA.render_frame(self.animation_object, obj.position)
        pass
