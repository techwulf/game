from source.abstract.app import app
from source.systems.universe import universe

class Game(app.App):
    def __init__(self):
        app.App.__init__(self)
        self.universe = universe.Universe()
        pass
