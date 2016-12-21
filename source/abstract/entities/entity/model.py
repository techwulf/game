import pygame
import math, uuid
from datetime import datetime, timedelta

class MoveState():
    STAND = 0

class Model:
    uuid = None
    created = None
    parent = None

    position = None

    direction = 0

    move_state = MoveState.STAND

    def __init__(self, parent):
        self.parent = parent
        self.uuid = uuid.uuid4()
        self.created = datetime.now()
        self.position = pygame.math.Vector3(0, 0, 0)
        pass
    
    def stand(self):
        self.move_state = MoveState.STAND
        pass

    def created_delta(self):
        return (datetime.now() - self.created).total_seconds()

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
