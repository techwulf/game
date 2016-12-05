import inanimate_entity_controller
import inanimate_entity_model
import inanimate_entity_view

class InanimateEntity(inanimate_entity_controller.AnimateEntityController, inanimate_entity_model.AnimateEntityModel, inanimate_entity_view.AnimateEntityView):
    def __init__(self):
        inanimate_entity_controller.InanimateEntityController.__init__(self)
        inanimate_entity_model.InanimateEntityModel.__init__(self)
        inanimate_entity_view.InanimateEntityView.__init__(self)
        pass
