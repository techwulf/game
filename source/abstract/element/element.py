class Element:
    name            = None
    symbol          = None
    atomic_number   = None
    group           = None
    period          = None
    atomic_weight   = None

    abundance       = {
        "universe"     : 0,
        "sun"          : 0,
        "crust"        : 0,
        "meteorite"    : 0,
        "ocean"        : 0,
        "human"        : 0
    }

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
