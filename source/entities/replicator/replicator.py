

class Replicator:
    elemental_storage_unit = None

    def __init__(self, esu):
        self.elemental_storage_unit = esu
        pass

    def build_widget(self):
        widget = Widget()

        if self.elemental_storage_unit.check_storage(widget.build_requierments):
            print("\033[94m"+"Building Widget"+"\033[0m")
            self.elemental_storage_unit.take_elements(widget.build_requierments)
            return Widget()
        else:
            print("\033[91m"+"Build Failed."+"\033[0m")
            return None
        pass


class Widget:
    name = "Widget"
    build_requierments = {
        "Iron"     : 1,
        "Aluminum" : 2,
        "Oxygen"   : 3,
        "Hydrogen" : 4
    }

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        pass
