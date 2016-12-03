from source.entities.entity import entity_view

from source.entities.entity import action

from animation_config import run
from animation_config import stand
from animation_config import walk

class TileView(entity_view.EntityView):
    def __init__(self):
        entity_view.EntityView.__init__(self)
        self.stand_action = action.Action(stand.stand_data)
        pass
