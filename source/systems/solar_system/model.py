from source.systems.planet import planet

class Model:
    parent = None
    planet = None

    def __init__(self, parent):
        self.parent = None
        self.planet = planet.Planet(self)
        pass
