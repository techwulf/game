from source.abstract.entities.inanimate import model

from datetime import datetime, timedelta

class Model(model.Model):
    charge = 0
    charge_time = 0

    def __init__(self, parent):
        model.Model.__init__(self, parent)
        self.charge_time = datetime.now()
        pass

    def delta_charge(self):
        self.charge += (datetime.now() - self.charge_time).total_seconds() / 100

    def discharge(self):
        c = self.charge
        self.charge = 0
        return c
