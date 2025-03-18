import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tile_selector import TileSelector

class InputPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.image_path = "path/to/your/input_tilemap.png"  # Replace with your image path
        self.image = None
        self.photo = None
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.load_image()

        self.tile_selector = TileSelector(self.canvas, self)
        self.selected_tile = None
        
        self.tile_scale = tk.IntVar(value=32)  # Default tile scale
        self.scale_label = ttk.Label(self, text="Tile Scale:")
        self.scale_label.pack()
        self.scale_entry = ttk.Entry(self, textvariable=self.tile_scale)
        self.scale_entry.pack()

        self.resize_larger_tiles = tk.BooleanVar(value=True)
        self.resize_check = ttk.Checkbutton(self, text="Resize Larger Tiles", variable=self.resize_larger_tiles)
        self.resize_check.pack()

        self.stack_selection_mode = tk.BooleanVar(value=False)
        self.stack_selection_check = ttk.Checkbutton(self, text="Stack Selection", variable=self.stack_selection_mode)
        self.stack_selection_check.pack()

    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.config(width=self.photo.width(), height=self.photo.height())
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.canvas.bind("<Control-Button-1>", self.tile_selector.start_selection)
            self.canvas.bind("<Control-B1-Motion>", self.tile_selector.update_selection)
            self.canvas.bind("<Control-ButtonRelease-1>", self.tile_selector.end_selection)
        except FileNotFoundError:
            print("Error: Input tilemap image not found.")

    def get_selected_tile(self):
        return self.selected_tile

    def set_selected_tile(self, tile_data):
        self.selected_tile = tile_data

    def get_tile_scale(self):
        return self.tile_scale.get()

    def should_resize_larger_tiles(self):
        return self.resize_larger_tiles.get()

    def get_stack_selection_mode(self):
        return self.stack_selection_mode.get()
