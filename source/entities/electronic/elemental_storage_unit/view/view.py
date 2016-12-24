from source.action import action

from source.abstract.entities.inanimate.view import view

from ..animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(stand.stand_data)
        pass
    
    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        
        for tank in self.tanks:
            self.tanks[tank].pretty_print(i+1)
        pass

    def on_render(self):
        view.View.on_render(self)
        for tank in self.tanks:
            self.tanks[tank].on_render()
        pass
