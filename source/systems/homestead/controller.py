class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        for entity in self.entities:
            entity.on_loop()
        pass

        self.power_grid.on_loop()
