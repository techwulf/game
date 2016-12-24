from source.action import action

from source.abstract.entities.inanimate.view import view

from ..animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        pass
