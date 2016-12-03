from source.entities.avatar import avatar
from source.entities.tile import tile

class Hectare:
    w = 100
    h = 100
    ground = [[0 for x in range(w)] for y in range(h)]
    entities = []

    def __init__(self):
        self.ground[0][0] = tile.Tile()
        self.ground[0][0].position.x -= 50
        self.entities = [
            tile.Tile(),
            avatar.Avatar()
        ]
        pass

    def on_render(self, surface, window):
        for entity in self.entities:
            entity.on_render(
                surface,
                window
            )
        self.ground[0][0].on_render(surface, window)
        pass

    def on_loop(self):
        self.ground[0][0].on_loop()
        for entity in self.entities:
            entity.on_loop()

    def boundary_check(self, window):
        for entity in self.entities:
            if entity.position.x < 0:
                entity.position.x = 0
            if entity.position.x > window.width - entity.width:
                entity.position.x = window.width - entity.width
            if entity.position.y < 0:
                entity.position.y = 0
            if entity.position.y > window.height - entity.height:
                entity.position.y = window.height - entity.height
        pass
