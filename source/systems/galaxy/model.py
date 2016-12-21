from source.systems.solar_system import solar_system

class Model:
    parent          = None
    solar_system    = None

    def __init__(self, parent):
        self.parent = None
        self.solar_system = solar_system.SolarSystem(self)
        pass
