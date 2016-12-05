import pygame
import math

from source.abstract.entity import entity_model

class MoveState():
    STAND = 0

class InanimateEntityModel(entity_model.EntityModel):
    def __init__(self):
        entity_model.EntityModel.__init__(self)
        pass
