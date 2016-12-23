import pygame
import math

from source.abstract.entities.animate import model

class Model(model.Model):
    holding = None
    reach   = 100
    
    def __init__(self, parent):
        model.Model.__init__(self, parent)
        pass

    def translate(self):
        model.Model.translate(self)
        if self.holding != None:
            self.holding.position.x = self.position.x
            self.holding.position.y = self.position.y
            self.holding.position.z = self.position.z

    def get_nearest_item(self):
        shortest_distance   = None
        item                = None
        for entity in self.parent.homestead.entities:
            distance = self.position.distance_to(entity.position)
            if distance < self.reach:
                if distance < shortest_distance or shortest_distance == None:
                    shortest_distance = distance
                    item = entity
        return item

    def drop_item(self):
        if self.holding != None:
            self.holding.position = self.holding.position
            self.holding.on_drop()
            self.holding = None
        pass

    def pickup(self):
        if self.holding == None:
            self.holding = self.get_nearest_item()
            if self.holding != None:
                self.holding.on_pickup()
        else:
            self.drop_item()
        pass
