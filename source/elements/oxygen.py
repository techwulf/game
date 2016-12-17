from source.abstract.element import element

class Oxygen(element.Element):
    name            = "Oxygen"
    symbol          = "O"
    atomic_number   = 8
    group           = 16
    period          = 2
    atomic_weight   = 15.999

    def __init__(self):
        element.Element.__init__(self)
        pass
