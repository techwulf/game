import elemental_storage_tank

class ElementalStorageUnit:
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

    def __init__(self):
        self.tanks["Aluminum"] = elemental_storage_tank.ElementalStorageTank("Aluminum")
        self.tanks["Carbon"] = elemental_storage_tank.ElementalStorageTank("Carbon")
        self.tanks["Hydrogen"] = elemental_storage_tank.ElementalStorageTank("Hydrogen")
        self.tanks["Iron"] = elemental_storage_tank.ElementalStorageTank("Iron")
        self.tanks["Oxygen"] = elemental_storage_tank.ElementalStorageTank("Oxygen")
        self.tanks["Silicon"] = elemental_storage_tank.ElementalStorageTank("Silicon")
        pass

    def store_element(self, element):
        self.tanks[element.name].add_element()
        pass

    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        
        for tank in self.tanks:
            self.tanks[tank].pretty_print(i+1)
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
