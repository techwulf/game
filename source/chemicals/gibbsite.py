from source.abstract.chemical import chemical

from source.elements import aluminum, oxygen, hydrogen

class Gibbsite(chemical.Chemical):
    name = "Gibbsite"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            aluminum.Aluminum(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen()
        ]
        pass
