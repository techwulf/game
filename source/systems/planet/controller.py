class Controller:
    def __init__(self):
        pass

    def on_loop(self):
        self.avatar.on_loop()
        self.homestead.on_loop()

        for kilometer in self.kilometers:
            for kilo in kilometer:
                kilo.on_loop()
        pass
