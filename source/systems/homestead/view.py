class View:
    def __init__(self):
        pass

    def on_render(self):
        for entity in self.entities:
            entity.on_render()
        self.logistics.on_render()
        pass
