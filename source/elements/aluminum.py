from source.abstract.element import element

class Aluminum(element.Element):
    name            = "Aluminum"
    symbol          = "Al"
    atomic_number   = 13
    group           = 13
    period          = 3
    atomic_weight   = 26.9815385

    def __init__(self):
        element.Element.__init__(self)
        pass
