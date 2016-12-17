from source.abstract.mineral import mineral

from source.chemicals import goethite, gibbsite

class Bauxite(mineral.Mineral):
    name = "Bauxite"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            goethite.Goethite(),
            gibbsite.Gibbsite()
        ]
