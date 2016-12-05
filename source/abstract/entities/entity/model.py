import pygame
import math

class MoveState():
    STAND = 0

class Model:
    position = None

    direction = 0

    move_state = MoveState.STAND

    def __init__(self):
        self.position = pygame.math.Vector3(0, 0, 0)
        pass
    
    def stand(self):
        self.move_state = MoveState.STAND
