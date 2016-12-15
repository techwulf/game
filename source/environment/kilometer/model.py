class Model:
    parent = None
    
    size = 10
    __hectares = [[None]]

    def __init__(self, parent):
        self.parent = parent
        self.populate_hectares()
        pass

    def populate_hectares(self):
        self.__hectares = [[None for x in range(self.size)] for y in range(self.size)]
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass
