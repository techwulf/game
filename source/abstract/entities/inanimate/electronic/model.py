import pygame
import math

from source.abstract.entities.inanimate import model

class MoveState():
    STAND = 0

class Model(model.Model):
    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass
