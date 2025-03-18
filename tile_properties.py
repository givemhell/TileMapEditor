class TileProperties:
    def __init__(self, output_panel):
        self.output_panel = output_panel
        self.properties = {}  # Store properties for each tile ID

    def get_properties(self, tile_id):
        return self.properties.get(tile_id, {})

    def set_properties(self, tile_id, props):
        self.properties[tile_id] = props

    def show_properties(self, tile_id):
        props = self.get_properties(tile_id)
        print(f"Properties for tile {tile_id}: {props}")
        # You can implement a UI to display and edit properties here
