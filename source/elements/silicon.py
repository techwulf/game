from source.abstract.element import element

class Silicon(element.Element):
    name            = "Silicon"
    symbol          = "Si"
    atomic_number   = 14
    group           = 14
    period          = 3
    atomic_weight   = 28.085

    def __init__(self):
        element.Element.__init__(self)
        pass
