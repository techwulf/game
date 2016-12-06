from source import global_variables
import animation

class Action:
    action = None
    entity_name = None
    north = None
    east = None
    west = None
    south = None

    def __init__(self, data):
        self.action = data["action"]
        self.entity_name = data["entity_name"]
        self.assign_directions(data)
        pass

    def assign_directions(self, data):
        for ani in data["animations"]:
            if ani["direction"] == "north":
                self.north = animation.Animation(data["entity_name"], data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "east":
                self.east = animation.Animation(data["entity_name"], data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "south":
                self.south = animation.Animation(data["entity_name"], data["action"], ani["direction"], ani["frames"])
            elif ani["direction"] == "west":
                self.west = animation.Animation(data["entity_name"], data["action"], ani["direction"], ani["frames"])
            else:
                print("Error: Avatar Animations Action not valid option")
        pass

    def on_render(self, camera, direction, position):
        if direction >= global_variables.NORTHWEST or direction <= global_variables.NORTHEAST:
            self.north.on_render(camera, position)
        elif direction >= global_variables.NORTHEAST and direction <= global_variables.SOUTHEAST:
            self.east.on_render(camera, position)
        elif direction >= global_variables.SOUTHEAST and direction <= global_variables.SOUTHWEST:
            self.south.on_render(camera, position)
        elif direction >= global_variables.SOUTHWEST and direction <= global_variables.NORTHWEST:
            self.west.on_render(camera, position)
        pass