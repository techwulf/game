from source.abstract.entities.inanimate.electronic.controller import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_refine(self, mineral):
        self.refine_mineral(mineral)
        pass
