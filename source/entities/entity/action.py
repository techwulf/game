from source import global_variables
import animation

class Action:
    name = None
    north = None
    east = None
    west = None
    south = None

    def __init__(self, data):
        self.assign_directions(data)
        pass

    def assign_directions(self, data):
        for ani in data["animations"]:
            if ani["direction"] == "north":
                self.north = animation.Animation(data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "east":
                self.east = animation.Animation(data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "south":
                self.south = animation.Animation(data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "west":
                self.west = animation.Animation(data["action"], ani["direction"], ani["frames"])
            else:
                print("Error: Avatar Animations Action not valid option")

    def render(self, surface, direction, position):
        if direction >= global_variables.NORTHWEST or direction <= global_variables.NORTHEAST:
            self.north.render(surface, position)
        elif direction >= global_variables.NORTHEAST and direction <= global_variables.SOUTHEAST:
            self.east.render(surface, position)
        elif direction >= global_variables.SOUTHEAST and direction <= global_variables.SOUTHWEST:
            self.south.render(surface, position)
        elif direction >= global_variables.SOUTHWEST and direction <= global_variables.NORTHWEST:
            self.west.render(surface, position)