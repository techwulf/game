from source.abstract.chemical import chemical

from source.elements import iron, oxygen

class IronIIOxide(chemical.Chemical):
    name = "IronII Oxide"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            iron.Iron(),
            oxygen.Oxygen(),
        ]
        pass
