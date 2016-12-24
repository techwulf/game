import controller, model, view

class Potato(controller.Controller, model.Model, view.View):
    def __init__(self, parent):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent)
        view.View.__init__(self)
        pass
