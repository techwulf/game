class Element:
    name            = None
    symbol          = None
    atomic_number   = None
    group           = None
    period          = None
    atomic_weight   = None

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
