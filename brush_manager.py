import tkinter as tk
from tkinter import ttk

class BrushManager(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.brush_size = tk.StringVar(value="Normal")
        self.brush_label = ttk.Label(self, text="Brush Size:")
        self.brush_label.pack(side=tk.LEFT)
        self.brush_dropdown = ttk.Combobox(self, textvariable=self.brush_size, values=["Normal", "32x", "64x", "128x"])
        self.brush_dropdown.pack(side=tk.LEFT)
