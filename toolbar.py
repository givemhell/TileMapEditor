import tkinter as tk
from tkinter import ttk
from brush_manager import BrushManager
from grid_customization import GridCustomization
from undo_redo import UndoRedoManager
from file_manager import FileManager  # Import FileManager
from tile_transformations import TileTransformations  # Import TileTransformations
from layer_manager import LayerManager
from tile_properties_panel import TilePropertiesPanel
from zoom_controls import ZoomControls

class Toolbar(ttk.Frame):
    def __init__(self, parent, output_panel):
        super().__init__(parent)
        self.parent = parent
        self.output_panel = output_panel

        self.undo_redo_manager = self.output_panel.undo_redo_manager

        self.undo_button = ttk.Button(self, text="Undo", command=self.undo_redo_manager.undo)
        self.undo_button.pack(side=tk.LEFT)
        self.redo_button = ttk.Button(self, text="Redo", command=self.undo_redo_manager.redo)
        self.redo_button.pack(side=tk.LEFT)

        self.brush_manager = BrushManager(self)
        self.brush_manager.pack(side=tk.LEFT)

        self.grid_customization = GridCustomization(self, self.output_panel)
        self.grid_customization.pack(side=tk.LEFT)

        self.file_manager = FileManager(self)
        self.file_manager.pack(side=tk.LEFT)

        self.tile_transformations = TileTransformations(self)
        self.tile_transformations.pack(side=tk.LEFT)

        self.layer_manager = LayerManager(self, self.output_panel.canvas)
        self.layer_manager.pack(side=tk.LEFT)

        self.tile_properties_panel = TilePropertiesPanel(self, self.output_panel.tile_properties)
        self.tile_properties_panel.pack(side=tk.LEFT)

        self.zoom_controls = ZoomControls(self, self.output_panel)
        self.zoom_controls.pack(side=tk.LEFT)
