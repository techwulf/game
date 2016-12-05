from source.pyganim import pyganim

class Animation:
    entity_name = None
    path_to_images = "resources/images/"
    action = None
    direction = None
    animation_object = None
    directory = None
    move_conductor = None

    def __init__(self, _entity_name, _action, _direction, _frames):
        self.entity_name = _entity_name
        self.action = _action
        self.direction = _direction
        self.load_frames(_frames)
        pass
    
    def path_to_animations(self):
        return self.path_to_images+self.entity_name+"/animations/"

    def load_frames(self, f):
        frames = []
        for fr in f:
            tmp_frame = self.path_to_animations()+self.action+'/'+self.direction+'/'+fr[0]
            tmp_duration = fr[1]
            fra = (tmp_frame, tmp_duration)
            frames.append(fra)
        self.animation_object = pyganim.PygAnimation(frames)
        self.move_conductor = pyganim.PygConductor(self.animation_object)
        pass

    def on_render(self, camera, position):
        self.move_conductor.play()
        self.animation_object.blit(
            camera.surface,
            (
                position.x,
                position.y
            )
        )
        pass
