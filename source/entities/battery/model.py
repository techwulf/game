from source.abstract.entities.inanimate import model

class ChargeState:
    PERCENT_000 = 0
    PERCENT_020 = 1
    PERCENT_040 = 2
    PERCENT_060 = 3
    PERCENT_080 = 4
    PERCENT_100 = 5

class Model(model.Model):
    charge = 0
    charge_state = ChargeState.PERCENT_000

    grid = None

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass
