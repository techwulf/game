class View:
    def __init__(self):
        pass

    def on_render(self):
        self.logistics.on_render()
        for entity in self.entities:
            entity.on_render()
        pass
