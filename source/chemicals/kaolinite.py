from source.abstract.chemical import chemical

from source.elements import aluminum, hydrogen, iron, oxygen, silicon

class Kaolinite(chemical.Chemical):
    name = "Kaolinite"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            aluminum.Aluminum(),
            aluminum.Aluminum(),
            silicon.Silicon(),
            silicon.Silicon(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            oxygen.Oxygen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen(),
            hydrogen.Hydrogen(),
        ]
        pass

# Al2Si2O5(OH)4
