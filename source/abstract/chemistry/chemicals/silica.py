from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements


# SiO2
class Silica(chemical.Chemical):
    name = "Silica"
    mass = 60.09
    density = 2.65

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Silicon(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        pass
