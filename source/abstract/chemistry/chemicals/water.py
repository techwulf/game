from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements


# H2O
class Water(chemical.Chemical):
    name = "Water"
    mass = 18.02
    density = 1.00

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen()
        ]
        pass
