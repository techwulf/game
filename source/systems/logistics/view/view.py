from source.abstract.entities.inanimate.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass
    
    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        
        for tank in self.tanks:
            self.tanks[tank].pretty_print(i+1)
        pass

    def on_render(self):
        self.elemental_storage_unit.on_render()
        self.refinery.on_render()
        self.replicator.on_render()
