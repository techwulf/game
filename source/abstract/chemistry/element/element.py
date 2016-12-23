class Element:
    name            = None
    symbol          = None
    mass            = None

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
