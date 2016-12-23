from source.abstract.chemistry.chemicals import water
from source.abstract.chemistry.mineral import mineral


class Ice(mineral.Mineral):
    name = "Ice"

    def __init__(self):
        mineral.Mineral.__init__(self)
        self.chemicals = [
            water.Water()
        ]
