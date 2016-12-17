from source.abstract.chemical import chemical

from source.elements import iron, oxygen

class IronIIIOxide(chemical.Chemical):
    name = "IronIII Oxide"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            iron.Iron(),
            iron.Iron(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen()
        ]
        pass
