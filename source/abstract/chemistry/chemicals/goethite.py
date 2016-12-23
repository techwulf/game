from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements


# FeO(OH)
class Goethite(chemical.Chemical):
    name = "Goethite"
    mass = 88.86
    density = 4.0  # 3.3 - 4.3

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen()
        ]
        pass
