from source.abstract.chemical import chemical

from source.elements import oxygen, hydrogen

class Water(chemical.Chemical):
    name = "Water"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            oxygen.Oxygen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen()
        ]
        pass
