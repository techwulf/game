
class View:
    def __init__(self):
        pass

    def on_render(self):
        self.camera.fill_surface()

        for kilometer in self.kilometers:
            for kilo in kilometer:
                kilo.on_render()
        
        self.homestead.on_render()
        self.avatar.on_render()
        #self.instructions.on_render()
        pass
