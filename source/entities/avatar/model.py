from source.abstract.entities.animate import model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class Model(model.Model):
    def __init__(self):
        model.Model.__init__(self)
        pass

    def run(self):
        self.move_state = MoveState.RUN
        pass

    def walk(self):
        self.move_state = MoveState.WALK
        pass
