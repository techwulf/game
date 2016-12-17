from source.abstract.element import element

class Iron(element.Element):
    name            = "Iron"
    symbol          = "Fe"
    atomic_number   = 26
    group           = 8
    period          = 4
    atomic_weight   = 55.845

    def __init__(self):
        element.Element.__init__(self)
        pass
