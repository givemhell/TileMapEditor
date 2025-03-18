import tkinter as tk
from tkinter import ttk
from tile_placer import TilePlacer
from layer_manager import LayerManager
from undo_redo import UndoRedoManager  # Import UndoRedoManager
from tile_properties import TileProperties  # Import TileProperties

class OutputPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.width = 512
        self.height = 384
        self.grid_size = 32  # Default grid size
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.layer_manager = LayerManager(self, self.canvas)
        self.tile_placer = TilePlacer(self.canvas, self, self.grid_size, self.layer_manager)
        self.undo_redo_manager = UndoRedoManager(self)  # Initialize UndoRedoManager
        self.tile_properties = TileProperties(self)

        self.canvas.bind("<Button-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.end_drag)
        self.canvas.bind("<Button-3>", self.select_tile)  # Right-click to select tile
        self.canvas.bind("<Control-Button-1>", self.start_move)  # Ctrl+Left-click to start move
        self.canvas.bind("<Control-B1-Motion>", self.move_tile)  # Ctrl+Left-drag to move
        self.canvas.bind("<Control-ButtonRelease-1>", self.end_move)  # Ctrl+Left-release to end move

        self.drag_start_x = None
        self.drag_start_y = None
        self.selected_tile_id = None  # Currently selected tile ID
        self.move_start_x = None
        self.move_start_y = None

        self.zoom_scale = 1.0  # Initial zoom scale
        self.canvas.bind("<MouseWheel>", self.zoom)  # Bind zoom to mouse wheel

    def start_drag(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
        input_panel = self.parent.input_panel
        selected_tile = input_panel.get_selected_tile()
        if selected_tile:
            self.tile_placer.start_placement(event.x, event.y, selected_tile)

    def drag(self, event):
        input_panel = self.parent.input_panel
        selected_tile = input_panel.get_selected_tile()
        if selected_tile:
            self.tile_placer.update_placement(event.x, event.y)

    def end_drag(self, event):
        input_panel = self.parent.input_panel
        selected_tile = input_panel.get_selected_tile()
        if selected_tile:
            tile_id = self.tile_placer.end_placement(event.x, event.y)
            if tile_id:
                self.undo_redo_manager.record_action(tile_id)

    def select_tile(self, event):
        input_panel = self.parent.input_panel
        stack_selection_mode = input_panel.get_stack_selection_mode()
        
        if stack_selection_mode:
            # Select from all tiles in the stack
            items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
            if items:
                if len(items) > 0:
                    self.selected_tile_id = items[-1]  # Select the top-most tile
                else:
                    self.selected_tile_id = None
            else:
                self.selected_tile_id = None
        else:
            # Select only the top-most visible tile
            self.selected_tile_id = self.canvas.find_closest(event.x, event.y)[0]
            
        print(f"Selected tile ID: {self.selected_tile_id}")
        self.tile_properties.show_properties(self.selected_tile_id)

    def start_move(self, event):
        self.selected_tile_id = self.canvas.find_closest(event.x, event.y)[0]
        self.move_start_x = event.x
        self.move_start_y = event.y
        print(f"Start moving tile ID: {self.selected_tile_id}")

    def move_tile(self, event):
        if self.selected_tile_id:
            dx = event.x - self.move_start_x
            dy = event.y - self.move_start_y
            self.canvas.move(self.selected_tile_id, dx, dy)
            self.move_start_x = event.x
            self.move_start_y = event.y

    def end_move(self, event):
        if self.selected_tile_id:
            print(f"End moving tile ID: {self.selected_tile_id}")
            self.selected_tile_id = None  # Deselect the tile
            self.move_start_x = None
            self.move_start_y = None

    def get_grid_size(self):
        return self.grid_size

    def set_grid_size(self, size):
        self.grid_size = size
        # Redraw the grid with the new size (implementation needed)
        self.redraw_grid()

    def redraw_grid(self):
        # Clear the existing grid lines
        self.canvas.delete("grid_line")

        # Calculate the current zoom level
        current_width = int(self.width * self.zoom_scale)
        current_height = int(self.height * self.zoom_scale)

        # Draw new grid lines based on the current grid size and zoom level
        for i in range(0, current_width, self.grid_size):
            self.canvas.create_line(i, 0, i, current_height, fill="lightgray", tags="grid_line")
        for j in range(0, current_height, self.grid_size):
            self.canvas.create_line(0, j, current_width, j, fill="lightgray", tags="grid_line")

    def zoom(self, event):
        if event.delta > 0:
            self.zoom_scale *= 1.1
        else:
            self.zoom_scale /= 1.1

        self.zoom_scale = max(0.1, min(self.zoom_scale, 5.0))  # Limit zoom scale

        self.canvas.scale("all", 0, 0, self.zoom_scale, self.zoom_scale)
        self.redraw_grid()  # Redraw grid after zooming

        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Update scroll region
