import tile_controller
import tile_model
import tile_view

class Tile(tile_controller.TileController, tile_model.TileModel, tile_view.TileView):
    def __init__(self):
        tile_controller.TileController.__init__(self)
        tile_model.TileModel.__init__(self)
        tile_view.TileView.__init__(self)