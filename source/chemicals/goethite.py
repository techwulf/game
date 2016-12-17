from source.abstract.chemical import chemical

from source.elements import iron, oxygen, hydrogen

class Goethite(chemical.Chemical):
    name = "Goethite"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            iron.Iron(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            hydrogen.Hydrogen()
        ]
        pass
