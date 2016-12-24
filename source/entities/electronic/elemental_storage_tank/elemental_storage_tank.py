from controller import controller
from model import model
from view import view

class ElementalStorageTank(controller.Controller, model.Model, view.View):
    def __init__(self, parent, element):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent, element)
        view.View.__init__(self)
        pass
