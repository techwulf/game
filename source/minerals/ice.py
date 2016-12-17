from source.abstract.mineral import mineral

from source.chemicals import water

class Ice(mineral.Mineral):
    name = "Ice"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            water.Water()
        ]
