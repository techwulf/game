from source.global_variables import global_variables
import animation

class Action:
    action      = None
    entity_name = None
    north       = None
    east        = None
    west        = None
    south       = None

    def __init__(self, data):
        self.action = data["action"]
        self.entity_name = data["entity_name"]
        self.assign_directions(data)
        pass

    def assign_directions(self, data):
        for ani in data["animations"]:
            if ani["direction"] == "north":
                self.north = animation.Animation(data, ani)
            elif ani["direction"] == "east":
                self.east = animation.Animation(data, ani)
            elif ani["direction"] == "south":
                self.south = animation.Animation(data, ani)
            elif ani["direction"] == "west":
                self.west = animation.Animation(data, ani)
            else:
                print("Error: Avatar Animations Action not valid option")
        pass

    def on_render(self, obj):
        if obj.direction >= global_variables.NORTHWEST or obj.direction <= global_variables.NORTHEAST:
            self.north.on_render(obj)
        elif obj.direction >= global_variables.NORTHEAST and obj.direction <= global_variables.SOUTHEAST:
            self.east.on_render(obj)
        elif obj.direction >= global_variables.SOUTHEAST and obj.direction <= global_variables.SOUTHWEST:
            self.south.on_render(obj)
        elif obj.direction >= global_variables.SOUTHWEST and obj.direction <= global_variables.NORTHWEST:
            self.west.on_render(obj)
        pass
