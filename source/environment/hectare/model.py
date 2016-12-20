from source.systems.power_grid import power_grid

from source.entities.avatar import avatar
from source.entities.rock import rock
from source.entities.tile import tile
from source.entities.corn import corn
from source.entities.turnip import turnip
from source.entities.tomato import tomato
from source.entities.potato import potato
from source.entities.npc import npc
from source.entities.solar_panel import solar_panel
from source.entities.battery import battery
from source.entities.lightbulb import lightbulb

class Model:
    coordinates     = (0,0)
    size            = 100
    entities        = []
    avatar          = None
    corn            = None
    turnip          = None
    tomato          = None
    potato          = None
    npc             = None
    rock            = None
    __tiles         = [[None]]

    solar_panel_0    = None
    solar_panel_1    = None
    battery         = None
    lightbulb       = None
    power_grid      = None

    def __init__(self):
        self.power_grid = power_grid.PowerGrid()

        self.avatar = avatar.Avatar(self)
        self.avatar.position.x = 300
        self.avatar.position.y = 300

        self.rock = rock.Rock(self)
        self.rock.position.x = 0
        self.rock.position.y = 300

        self.corn = corn.Corn(self)
        self.corn.position.x = 100
        self.corn.position.y = 200

        self.turnip = turnip.Turnip(self)
        self.turnip.position.x = 300
        self.turnip.position.y = 200
        
        self.tomato = tomato.Tomato(self)
        self.tomato.position.x = 200
        self.tomato.position.y = 200

        self.potato = potato.Potato(self)
        self.potato.position.x = 400
        self.potato.position.y = 200

        self.npc = npc.NPC(self)
        self.npc.position.x = 0
        self.npc.position.y = 200

        self.solar_panel_0 = solar_panel.SolarPanel(self)
        self.solar_panel_0.position.x = 0
        self.solar_panel_0.position.y = 0
        self.power_grid.attach_source(self.solar_panel_0)

        self.solar_panel_1 = solar_panel.SolarPanel(self)
        self.solar_panel_1.position.x = 0
        self.solar_panel_1.position.y = 100
        self.power_grid.attach_source(self.solar_panel_1)

        self.battery = battery.Battery(self)
        self.battery.position.x = 100
        self.battery.position.y = 0
        self.battery.charge = 21
        self.power_grid.attach_store(self.battery)

        self.lightbulb = lightbulb.LightBulb(self)
        self.lightbulb.position.x = 200
        self.lightbulb.position.y = 0
        self.power_grid.attach_drain(self.lightbulb)

        self.populate_ground_tiles()

        self.entities = [
            self.rock,
            self.corn,
            self.turnip,
            self.tomato,
            self.potato,
            self.npc,
            self.solar_panel_0,
            self.solar_panel_1,
            self.battery,
            self.lightbulb,
            self.avatar,
        ]
        pass

    def get_tile(self, x, y):
        if x < self.size and y < self.size:
            if self.__tiles[x][y] == None:
                self.__tiles[x][y] = tile.Tile(self)
                self.__tiles[x][y].position.x = (x * self.__tiles[x][y].width)
                self.__tiles[x][y].position.y = (y * self.__tiles[x][y].height)
            return self.__tiles[x][y]
        return None
    
    def populate_ground_tiles(self):
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
