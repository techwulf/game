

class ElementalStorageTank:
    element  = None
    units    = 0
    capacity = 10

    def __init__(self, element):
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

    def pretty_print(self, i=0):
        print(("\t"*i)+self.element+" "+str(self.units)+"/"+str(self.capacity))
