from source.entities.avatar import avatar
from source.entities.tile import tile

class Hectare:
    w        = 10
    h        = 10
    ground   = [[]]
    entities = []
    avatar   = None

    def __init__(self):
        self.avatar = avatar.Avatar()

        self.ground = [[tile.Tile() for x in range(self.w)] for y in range(self.h)]

        i = 0
        j = 0
        for row in self.ground:
            for t in row:
                t.position.x = (i * t.width)
                t.position.y = (j * t.height)
                i+=1
            i=0
            j+=1

        self.entities = [
            self.avatar
        ]
        pass

    def get_renderable_tiles(self, camera):
        tile_size = 100 #TODO: Bad magic numbers
        x = int(camera.position.x / tile_size)
        y = int(camera.position.y / tile_size)
        w = int((camera.position.x + camera.resolution.x) / tile_size) + 1
        h = int((camera.position.y + camera.resolution.y) / tile_size) + 1
        return list(map(lambda row: row[x:w], self.ground[y:h]))

    def on_render(self, camera):
        for row in self.get_renderable_tiles(camera):
            for t in row:
                if camera.in_viewport(t):
                    t.on_render(camera)
        
        for entity in self.entities:
            entity.on_render(
                camera
            )
        pass

    def on_loop(self):
        for row in self.ground:
            for t in row:
                t.on_loop()
        
        for entity in self.entities:
            entity.on_loop()
