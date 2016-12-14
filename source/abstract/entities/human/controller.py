from source import global_variables
from source.interface import keyboard
from source.abstract.entities.animate import controller

class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        pass
