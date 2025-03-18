import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

class GridCustomization(ttk.Frame):
    def __init__(self, parent, output_panel):
        super().__init__(parent)
        self.parent = parent
        self.output_panel = output_panel

        self.grid_visible = tk.BooleanVar(value=True)
        self.grid_visible_check = ttk.Checkbutton(self, text="Grid Visible", variable=self.grid_visible, command=self.toggle_grid)
        self.grid_visible_check.pack(side=tk.LEFT)

        self.grid_color_button = ttk.Button(self, text="Grid Color", command=self.choose_color)
        self.grid_color_button.pack(side=tk.LEFT)

        self.grid_size_label = ttk.Label(self, text="Grid Size:")
        self.grid_size_label.pack(side=tk.LEFT)
        self.grid_size = tk.IntVar(value=32)
        self.grid_size_entry = ttk.Entry(self, textvariable=self.grid_size)
        self.grid_size_entry.pack(side=tk.LEFT)
        self.grid_size_entry.bind("<FocusOut>", self.update_grid_size)

        self.grid_alpha_label = ttk.Label(self, text="Grid Alpha:")
        self.grid_alpha_label.pack(side=tk.LEFT)
        self.grid_alpha = tk.DoubleVar(value=1.0)
        self.grid_alpha_scale = tk.Scale(self, variable=self.grid_alpha, from_=0.0, to=1.0, resolution=0.05, orient=tk.HORIZONTAL, command=self.update_grid_alpha)
        self.grid_alpha_scale.pack(side=tk.LEFT)

        self.grid_color = "lightgray"  # Default grid color

    def toggle_grid(self):
        if self.grid_visible.get():
            self.output_panel.redraw_grid()
        else:
            self.output_panel.canvas.delete("grid_line")

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose grid color", color=self.grid_color)
        if color_code[1]:
            self.grid_color = color_code[1]
            self.output_panel.redraw_grid()

    def update_grid_size(self, event=None):
        try:
            size = int(self.grid_size.get())
            self.output_panel.set_grid_size(size)
        except ValueError:
            print("Invalid grid size")

    def update_grid_alpha(self, value):
        self.output_panel.redraw_grid()
