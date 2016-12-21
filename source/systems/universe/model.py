from source.systems.galaxy import galaxy

class Model:
    parent  = None
    galaxy  = None

    def __init__(self, parent):
        self.parent = None
        self.galaxy = galaxy.Galaxy(self)
        pass
