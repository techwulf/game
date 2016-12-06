from source.interface import camera, instructions
from source.environment.hectare import hectare

class Planet:
    camera  = None
    hectare = None
    instructions    = None

    def __init__(self, window):
        self.hectare = hectare.Hectare()
        self.instructions = instructions.Instructions(window)
        self.camera = camera.Camera(window)
        self.camera.set_target(self.hectare.avatar)
        pass

    def on_render(self):
        self.camera.fill_surface()
        self.hectare.on_render(self.camera)
        self.instructions.on_render(self.camera)

    def on_loop(self):
        self.hectare.on_loop()
        pass
