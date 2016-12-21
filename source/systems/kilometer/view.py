class View:
    def __init__(self):
        pass

    def on_render(self):
        for hectare in self.hectares:
            for hect in hectare:
                hect.on_render()
