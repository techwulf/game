import avatar_controller
import avatar_model
import avatar_view

class Avatar(avatar_controller.AvatarController, avatar_model.AvatarModel, avatar_view.AvatarView):
    def __init__(self):
        avatar_controller.AvatarController.__init__(self)
        avatar_model.AvatarModel.__init__(self)
        avatar_view.AvatarView.__init__(self)