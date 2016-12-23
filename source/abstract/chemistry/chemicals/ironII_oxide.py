from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements

# FeO
class IronIIOxide(chemical.Chemical):
    name = "IronII Oxide"
    mass = 71.85
    density = 5.75

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Iron(),
            elements.Oxygen()
        ]
        pass
