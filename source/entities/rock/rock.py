import rock_controller
import rock_model
import rock_view

class Rock(rock_controller.RockController, rock_model.RockModel, rock_view.RockView):
    def __init__(self):
        rock_controller.RockController.__init__(self)
        rock_model.RockModel.__init__(self)
        rock_view.RockView.__init__(self)
        pass
