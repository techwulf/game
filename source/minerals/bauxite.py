from source.abstract.mineral import mineral

from source.chemicals import goethite, gibbsite, boehmite, ironII_oxide, ironIII_oxide, kaolinite

class Bauxite(mineral.Mineral):
    name = "Bauxite"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            goethite.Goethite(),
            gibbsite.Gibbsite(),
            boehmite.Boehmite(),
            ironII_oxide.IronIIOxide(),
            ironIII_oxide.IronIIIOxide(),
            kaolinite.Kaolinite()
        ]
