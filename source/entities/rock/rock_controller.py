from source.abstract.inanimate_entity import inanimate_entity_controller

class RockController(inanimate_entity_controller.InanimateEntityController):
    def __init__(self):
        inanimate_entity_controller.InanimateEntityController.__init__(self)
        pass

    def on_loop(self):
        pass
