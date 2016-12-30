from source.abstract.entities.inanimate.electronic.model import model

class Model(model.Model):
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def refine_mineral(self, mineral):
        print("\033[94m"+"Refining "+mineral.name+" and Storing it's Elements in the Elemental Storage Unit."+"\033[0m")
        for chemical in mineral.chemicals:
            for element in chemical.elements:
                self.parent.elemental_storage_unit.store_element(element)
        pass
