import pygame
import source.pyganim.pyganim as pyganim

class Animation:
    file = None
    path_to_images = 'resources/images/'
    action = None
    direction = None
    animation_object = None
    directory = None
    move_conductor = None

    def __init__(self, _action, _direction, _frames):
        self.action = _action
        self.direction = _direction
        self.load_frames(_frames)
    
    def load_frames(self, f):
        frames = []
        for fr in f:
            tmp_frame = self.path_to_images+self.action+'/'+self.direction+'/'+fr[0]
            tmp_duration = fr[1]
            fra = (tmp_frame, tmp_duration)
            frames.append(fra)
        self.animation_object = pyganim.PygAnimation(frames)
        self.move_conductor = pyganim.PygConductor(self.animation_object)

    def render(self, surface, position):
        self.move_conductor.play()
        self.animation_object.blit(
            surface,
            (
                position.x,
                position.y
            )
        )