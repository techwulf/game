
class PowerGrid:
    sources = []
    stores  = []
    drains   = []

    grid = None

    def __init__(self):
        pass

    def attach_source(self, obj):
        obj.grid = self
        self.sources.append(obj)
        pass

    def attach_store(self, obj):
        obj.grid = self
        self.stores.append(obj)
        pass

    def attach_drain(self, obj):
        obj.grid = self
        self.drains.append(obj)
        pass

    def charge(self):
        charge = 0
        for source in self.sources:
            source.delta_charge()
            charge += source.charge
            source.charge = 0

        for store in self.stores:
            #TODO: This will charge all stores with the charge amount. Instead, it should divide amongst the stores / charge
            #TODO: Check if adding a charge will go over 100%, if so, add to a different source
            #TODO: Overcharging damages store?
            store.charge += charge
        pass

    def discharge(self, i):
        charge = 0
        for store in self.stores:
            if store.charge >= i:
                store.charge -= i
                charge += i
            else:
                charge += store.charge
                store.charge = 0
        return charge

    def on_loop(self):
        self.charge()

        for drain in self.drains:
            drain.discharge()
        pass
