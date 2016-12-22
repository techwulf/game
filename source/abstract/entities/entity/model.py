import pygame
from source.abstract.base_object import base_model

class MoveState():
    STAND = 0

class Model(base_model.BaseModel):
    position = None

    direction = 0

    move_state = MoveState.STAND

    def __init__(self, parent):
        base_model.BaseModel.__init__(self, parent)
        self.position = pygame.math.Vector3(0, 0, 0)
        pass
    
    def stand(self):
        self.move_state = MoveState.STAND
        pass

    def get_kilometer(self):
        return (
            math.floor(self.position.x / 10000),
            math.floor(self.position.y / 10000)
        )

    def get_hectare(self):
        return (
            math.floor(self.position.x / 1000),
            math.floor(self.position.y / 1000)
        )

    def get_tile(self):
        return (
            math.floor(self.position.x / 100),
            math.floor(self.position.y / 100)
        )
