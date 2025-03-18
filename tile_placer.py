import tkinter as tk
from PIL import ImageTk, Image

class TilePlacer:
    def __init__(self, canvas, output_panel, grid_size, layer_manager):
        self.canvas = canvas
        self.output_panel = output_panel
        self.tile_image = None
        self.ghost_image_id = None
        self.grid_size = grid_size
        self.layer_manager = layer_manager

    def start_placement(self, x, y, tile_data):
        input_panel = self.output_panel.parent.input_panel
        tile_scale = input_panel.get_tile_scale()
        resize_larger_tiles = input_panel.should_resize_larger_tiles()
        
        brush_size = self.get_brush_size()
        
        if brush_size != "Normal":
            size = int(brush_size.replace("x", ""))
            tile_data = tile_data.resize((size, size), Image.Resampling.NEAREST)
        else:
            width, height = tile_data.size
            if resize_larger_tiles and (width > tile_scale or height > tile_scale):
                tile_data = tile_data.resize((tile_scale, tile_scale), Image.Resampling.NEAREST)

            else:
                tile_data = tile_data.resize((width, height), Image.Resampling.NEAREST)

        self.tile_image = ImageTk.PhotoImage(tile_data)
        self.ghost_image_id = self.canvas.create_image(self.snap_to_grid(x), self.snap_to_grid(y), image=self.tile_image, anchor=tk.NW)
        self.canvas.itemconfig(self.ghost_image_id, state='hidden')

    def update_placement(self, x, y):
        if self.ghost_image_id:
            self.canvas.coords(self.ghost_image_id, self.snap_to_grid(x), self.snap_to_grid(y))
            self.canvas.itemconfig(self.ghost_image_id, state='normal')

    def end_placement(self, x, y):
        if self.ghost_image_id:
            self.canvas.itemconfig(self.ghost_image_id, state='normal')
            self.canvas.delete(self.ghost_image_id)
            self.ghost_image_id = None
            tile_id = self.place_tile(self.snap_to_grid(x), self.snap_to_grid(y), self.tile_image)
            self.tile_image = None
            return tile_id
        return None

    def place_tile(self, x, y, tile_image):
        layer_id = self.layer_manager.get_current_layer()
        tile_id = self.canvas.create_image(x, y, image=tile_image, anchor=tk.NW, tags=layer_id)
        print(f"Tile placed at: ({x}, {y}) on layer {layer_id}")
        return tile_id

    def snap_to_grid(self, coord):
        return coord - coord % self.grid_size
    
    def get_brush_size(self):
         return self.output_panel.parent.toolbar.brush_manager.brush_size.get()
