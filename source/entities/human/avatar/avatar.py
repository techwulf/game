from controller import controller
from model import model
from view import view

class Avatar(controller.Controller, model.Model, view.View):
    def __init__(self, parent):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent)
        view.View.__init__(self)
