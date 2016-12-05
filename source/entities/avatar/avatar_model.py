from source.abstract.entity import entity_model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class AvatarModel(entity_model.EntityModel):
    def __init__(self):
        entity_model.EntityModel.__init__(self)
        pass

    def run(self):
        self.move_state = MoveState.RUN

    def walk(self):
        self.move_state = MoveState.WALK
