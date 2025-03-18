import tkinter as tk
from tkinter import ttk

class ZoomControls(ttk.Frame):
    def __init__(self, parent, output_panel):
        super().__init__(parent)
        self.parent = parent
        self.output_panel = output_panel

        self.zoom_in_button = ttk.Button(self, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT)

        self.zoom_out_button = ttk.Button(self, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.LEFT)

        self.zoom_reset_button = ttk.Button(self, text="Reset Zoom", command=self.reset_zoom)
        self.zoom_reset_button.pack(side=tk.LEFT)

    def zoom_in(self):
        self.output_panel.zoom(delta=1)

    def zoom_out(self):
        self.output_panel.zoom(delta=-1)

    def reset_zoom(self):
        self.output_panel.zoom_scale = 1.0
        self.output_panel.canvas.scale("all", 0, 0, 1.0, 1.0)
        self.output_anel.redraw_grid()
