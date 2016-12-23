from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements


# Fe(III)2O3
class Hematite(chemical.Chemical):
    name = "Hematite"
    mass = 159.70
    density = 5.26

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen()
        ]
        pass
