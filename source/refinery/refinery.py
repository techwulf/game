

class Refinery:
    elemental_storage_unit = None

    def __init__(self, esu):
        self.elemental_storage_unit = esu
        pass

    def refine_mineral(self, mineral):
        print("\033[94m"+"Refining "+mineral.name+" and Storing it's Elements in the Elemental Storage Unit."+"\033[0m")
        for chemical in mineral.chemicals:
            for element in chemical.elements:
                self.elemental_storage_unit.store_element(element)
        pass
