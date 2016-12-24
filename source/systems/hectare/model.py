from source.entities.inanimate.tile import tile

class Model:
    parent      = None
    position    = (0, 0)
    size        = 100
    entities    = []
    
    __tiles     = [[None]]

    def __init__(self, parent):
        self.parent = parent
        self.populate_tiles()
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_hectare(self):
        return self

    def get_kilometer(self):
        return self.parent.get_kilometer()

    def get_planet(self):
        return self.parent.get_planet()

    def get_tile(self, x, y):
        if x < self.size and y < self.size:
            if self.__tiles[x][y] == None:
                self.__tiles[x][y] = tile.Tile(self)
                self.__tiles[x][y].position.x = (x * self.__tiles[x][y].width)
                self.__tiles[x][y].position.y = (y * self.__tiles[x][y].height)
            return self.__tiles[x][y]
        return None
    
    def populate_tiles(self):
        self.__tiles = [[None for x in range(self.size)] for y in range(self.size)]
        pass
    
    def get_tiles(self, a):
        x = a[0]
        y = a[1]
        w = a[2]
        h = a[3]

        if x <= 0:
            x = 0
        if y <= 0:
            y = 0

        tmp_tiles = [[self.get_tile(k, l) for k in range(x, x+w)] for l in range(y, y+h)]
        return tmp_tiles

    def convert_pixel_dimensions_to_tile_dimensions(self, a, b, c, d):
        tile_width = self.get_tile(0, 0).width
        tile_height = self.get_tile(0, 0).height
        x = int((a - (c / 2)) / tile_width)
        y = int((b - (d / 2)) / tile_height)
        w = int((c + (c)) / tile_width) + 1
        h = int((d + (d)) / tile_height) + 1
        return (x, y, w, h)
    
    def get_near_tiles(self, obj):
        return self.get_tiles(
            self.convert_pixel_dimensions_to_tile_dimensions(
                obj.position.x,
                obj.position.y,
                obj.resolution.x,
                obj.resolution.y
            )
        )
        pass
