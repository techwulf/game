from source.abstract.entities.inanimate import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        self.discharge()
        pass
