from source.abstract.element import element

class Carbon(element.Element):
    name            = "Carbon"
    symbol          = "C"
    atomic_number   = 6
    group           = 14
    period          = 2
    atomic_weight   = 12.011

    def __init__(self):
        element.Element.__init__(self)
        pass
