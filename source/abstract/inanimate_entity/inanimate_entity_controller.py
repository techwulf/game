from source import global_variables
from source.interface import keyboard
from source.abstract.entity import entity_controller

class InanimateEntityController(entity_controller.EntityController):
    def __init__(self):
        entity_controller.EntityController.__init__(self)
        pass
