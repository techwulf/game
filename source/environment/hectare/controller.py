class Controller:
    def __init__(self):
        pass

    def on_render(self, camera):
        for row in self.get_near_tiles(camera):
            for t in row:
                if t != None:
                    if camera.in_viewport(t):
                        t.on_render(camera)
            
        for entity in self.entities:
            entity.on_render(
                camera
            )
        pass

    def on_loop(self):
        for row in self.get_near_tiles(self.avatar):
            for t in row:
                if t != None:
                    t.on_loop()
        
        for entity in self.entities:
            entity.on_loop()
        pass

        self.power_grid.on_loop()
