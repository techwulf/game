from source.entities.avatar import avatar
from source.entities.rock import rock
from source.entities.tile import tile

class Hectare:
    coordinates = (0,0)
    w        = 10
    h        = 10
    ground   = [[]]
    entities = []
    avatar   = None
    rock     = None

    def __init__(self):
        self.avatar = avatar.Avatar(self)
        self.rock = rock.Rock()
        self.rock.position.x = 523
        self.rock.position.y = 521

        self.populate_ground_tiles()

        self.entities = [
            self.avatar,
            self.rock
        ]
        pass

    def populate_ground_tiles(self):
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
        pass

    def get_renderable_tiles(self, camera):
        tile_width = self.ground[0][0].width
        tile_height = self.ground[0][0].height
        x = int((camera.position.x - (camera.resolution.x / 2)) / tile_width)
        y = int((camera.position.y - (camera.resolution.y / 2)) / tile_height)
        w = int(camera.resolution.x / tile_width)
        h = int(camera.resolution.y / tile_height)

        if x <= 0:
            x=0
        if y <= 0:
            y=0
        
        l = list(map(lambda row: row[x:x+w+1], self.ground[y:y+h+1]))
        return l

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
