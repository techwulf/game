from source.abstract.entities.inanimate import model

class UseState:
    OFF = 0
    ON  = 1

class Model(model.Model):
    use_state = UseState.OFF

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass

    def discharge(self):
        if self.use_state == UseState.ON:
            self.parent.battery.charge -= .5
