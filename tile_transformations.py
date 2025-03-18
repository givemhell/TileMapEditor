import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TileTransformations(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.output_panel = parent.parent.output_panel
        self.input_panel = parent.parent.input_panel

        self.rotate_left_button = ttk.Button(self, text="Rotate Left", command=self.rotate_left)
        self.rotate_left_button.pack(side=tk.LEFT)

        self.rotate_right_button = ttk.Button(self, text="Rotate Right", command=self.rotate_right)
        self.rotate_right_button.pack(side=tk.LEFT)

        self.flip_horizontal_button = ttk.Button(self, text="Flip Horizontal", command=self.flip_horizontal)
        self.flip_horizontal_button.pack(side=tk.LEFT)

        self.flip_vertical_button = ttk.Button(self, text="Flip Vertical", command=self.flip_vertical)
        self.flip_vertical_button.pack(side=tk.LEFT)

    def rotate_left(self):
       self.transform_tile(Image.ROTATE_270)

    def rotate_right(self):
        self.transform_tile(Image.ROTATE_90)

    def flip_horizontal(self):
        self.transform_tile(Image.FLIP_LEFT_RIGHT)

    def flip_vertical(self):
        self.transform_tile(Image.FLIP_TOP_BOTTOM)

    def transform_tile(self, method):
        selected_tile = self.input_panel.get_selected_tile()
        if selected_tile:
            transformed_tile = selected_tile.transpose(method)
            self.input_panel.set_selected_tile(transformed_tile)
            # Update the displayed image in the input panel (if needed)
            self.update_input_panel_image(transformed_tile)

    def update_input_panel_image(self, self, text="Save Properties", command=self.save_properties)
        self.save_button.pack()

    def set_tile_id(self, tile_id):
        self.tile_id = tile_id
        if tile_id:
            props = self.tile_properties.get_properties(tile_id)
            self.collision_var.set(props.get("collision", ""))
            self.interaction_var.set(props.get("interaction", ""))
            self.object_type_var.set(props.get("object_type", ""))
        else:
            self.clear_fields()

    def save_properties(self):
        if self.tile_id:
            props = {
                "collision": self.collision_var.get(),
                "interaction": self.interaction_var.get(),
                "object_type": self.object_type_var.get()
            }
            self.tile_properties.set_properties(self.tile_id, props)
            print(f"Saved properties for tile {self.tile_id}: {props}")

    def clear_fields(self):
        self.collision_var.set("")
        self.interaction_var.set("")
        self.object_type_var.set("")
