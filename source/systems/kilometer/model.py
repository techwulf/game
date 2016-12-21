from source.systems.hectare import hectare

class Model:
    parent      = None
    position    = (0, 0)
    size        = 1
    hectares  = [[None]]

    def __init__(self, parent):
        self.parent = parent
        self.populate_hectares()
        pass

    def populate_hectares(self):
        self.hectares = [[hectare.Hectare(self) for x in range(self.size)] for y in range(self.size)]
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_hectare(self, x, y):
        return self.hectares(x, y)

    def get_kilometer(self):
        return self

    def get_planet(self):
        return self.parent
