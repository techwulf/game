from source.abstract.element import element

class Hydrogen(element.Element):
    name            = "Hydrogen"
    symbol          = "H"
    atomic_number   = 1
    group           = 1
    period          = 1
    atomic_weight   = 1.008

    def __init__(self):
        element.Element.__init__(self)
        pass
