from source.interface import camera, instructions
from source.environment.kilometer import kilometer
from source.environment.hectare import hectare

class Planet:
    camera          = None
    hectare         = None
    instructions    = None

    size            = 10
    __kilometers    = [[None]]
    
    def __init__(self, window):
        self.populate_kilometers()

        self.hectare = hectare.Hectare()
        self.instructions = instructions.Instructions(window)
        self.camera = camera.Camera(window)
        self.camera.set_target(self.hectare.avatar)
        pass

    def populate_kilometers(self):
        self.__kilometers = [[None for x in range(self.size)] for y in range(self.size)]
        pass

    def on_render(self):
        self.camera.fill_surface()
        self.hectare.on_render(self.camera)
        self.instructions.on_render(self.camera)
        pass

    def on_loop(self):
        self.hectare.on_loop()
        pass
