from source.abstract.entities.inanimate.model import model

class CapacityState:
    PERCENT_000 = 0
    PERCENT_020 = 1
    PERCENT_040 = 2
    PERCENT_060 = 3
    PERCENT_080 = 4
    PERCENT_100 = 5

class Model(model.Model):
    element  = None
    units    = 0
    capacity = 10
    capacity_state = CapacityState.PERCENT_000

    def __init__(self, parent, element):
        model.Model.__init__(self, parent)
        self.element = element
        pass

    def add_element(self):
        if self.units == self.capacity:
            print("\033[91m"+self.element+" Storage Tank is Full. "+self.element+" Has Been Wasted.\033[0m")
        else:
            print("\033[92m"+self.element+" Stored.\033[0m")
            self.units+=1
        pass

    def remove_elements(self, amount):
        self.units -= amount
