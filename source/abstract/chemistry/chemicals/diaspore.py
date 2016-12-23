from source.abstract.chemistry.chemical import chemical
from source.abstract.chemistry.element import elements

# α-AlO(OH)
class Diaspore(chemical.Chemical):
    name = "Diaspore"
    mass = 59.99
    density = 3.25  # 3.1 - 3.4

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen()
        ]
        pass


