from source.systems.power_grid import power_grid
from source.entities.plant.corn import corn
from source.entities.plant.turnip import turnip
from source.entities.plant.tomato import tomato
from source.entities.plant.potato import potato
from source.entities.human.npc import npc
from source.entities.electronic.solar_panel import solar_panel
from source.entities.electronic.battery import battery
from source.entities.electronic.lightbulb import lightbulb
from source.entities.inanimate.rock import rock
from source.systems.logistics import logistics

class Model:
    entities        = []
    power_grid      = None
    logistics       = None
    corn            = None
    turnip          = None
    tomato          = None
    potato          = None
    npc             = None
    rock            = None

    def __init__(self):
        self.power_grid = power_grid.PowerGrid()

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

        self.npc = npc.NPC(self)
        self.npc.position.x = 0
        self.npc.position.y = 200

        self.logistics = logistics.Logistics(self)
        self.logistics.refinery.position.x = 0
        self.logistics.refinery.position.y = 400
        self.logistics.elemental_storage_unit.position.x = 100
        self.logistics.elemental_storage_unit.position.y = 400
        self.logistics.replicator.position.x = 200
        self.logistics.replicator.position.y = 400

        x = 0
        for tank in self.logistics.elemental_storage_unit.tanks:
            self.logistics.elemental_storage_unit.tanks[tank].position.x = x
            self.logistics.elemental_storage_unit.tanks[tank].position.y = 500
            x += 50

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
            self.lightbulb
        ]

        pass
