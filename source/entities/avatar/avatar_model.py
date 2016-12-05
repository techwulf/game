from source.abstract.animate_entity import animate_entity_model

class MoveState():
    STAND = 0
    WALK = 1
    RUN = 2

class AvatarModel(animate_entity_model.AnimateEntityModel):
    def __init__(self):
        animate_entity_model.AnimateEntityModel.__init__(self)
        pass

    def run(self):
        self.move_state = MoveState.RUN
        pass

    def walk(self):
        self.move_state = MoveState.WALK
        pass
