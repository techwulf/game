from libs.pyganim import pyganim

class Animation:
    entity_name = None
    path_to_images = "resources/images/"
    action = None
    direction = None
    animation_object = None
    directory = None
    move_conductor = None

    def __init__(self, data, animation):
        self.entity_name    = data["entity_name"]
        self.action         = data["action"]
        self.direction      = animation["direction"]
        self.load_frames(animation["frames"])
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

    def on_render(self, camera, obj):
        self.move_conductor.play()
        camera.render_object(self.animation_object, obj.position)
        pass
