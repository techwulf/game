from source.abstract.entities.inanimate.electronic.model import model

from source.entities.electronic.elemental_storage_tank import elemental_storage_tank

class Model(model.Model):
    name = "Elemental Storage Unit"
    elements = []
    
    tanks = {
        "Aluminum" : None,
        "Carbon"   : None,
        "Hydrogen" : None,
        "Iron"     : None,
        "Oxygen"   : None,
        "Silicon"  : None,
    }
    
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.tanks["Aluminum"] = elemental_storage_tank.ElementalStorageTank(self, "Aluminum")
        self.tanks["Carbon"] = elemental_storage_tank.ElementalStorageTank(self, "Carbon")
        self.tanks["Hydrogen"] = elemental_storage_tank.ElementalStorageTank(self, "Hydrogen")
        self.tanks["Iron"] = elemental_storage_tank.ElementalStorageTank(self, "Iron")
        self.tanks["Oxygen"] = elemental_storage_tank.ElementalStorageTank(self, "Oxygen")
        self.tanks["Silicon"] = elemental_storage_tank.ElementalStorageTank(self, "Silicon")
        pass

    def store_element(self, element):
        self.tanks[element.name].add_element()
        pass

    def check_storage(self, requirements):
        print("\033[92m"+"Checking Storage To See If There Are Enough Elements To Build."+".\033[0m")
        for requirement in requirements:
            if self.tanks[requirement].units < requirements[requirement]:
                print("\033[91m"+"Storage Tank Does Not Have Enough. "+requirement+"\033[0m")
                return False
        return True

    def take_elements(self, requirements):
        for requirement in requirements:
            self.tanks[requirement].remove_elements(requirements[requirement])
