import animate_entity_controller
import animate_entity_model
import animate_entity_view

class AnimateEntity(animate_entity_controller.AnimateEntityController, animate_entity_model.AnimateEntityModel, animate_entity_view.AnimateEntityView):
    def __init__(self):
        animate_entity_controller.AnimateEntityController.__init__(self)
        animate_entity_model.AnimateEntityModel.__init__(self)
        animate_entity_view.AnimateEntityView.__init__(self)
        pass
