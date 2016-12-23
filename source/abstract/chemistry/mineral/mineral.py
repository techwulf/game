class Mineral:
    name = None
    chemicals = [None]
    
    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
        for chemical in self.chemicals:
            chemical.pretty_print(i+1)
