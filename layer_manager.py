import tkinter as tk
from tkinter import ttk

class LayerManager(ttk.Frame):
    def __init__(self, parent, canvas):
        super().__init__(parent)
        self.parent = parent
        self.canvas = canvas
        self.layers = ["background", "midground", "foreground"]
        self.current_layer = "midground"
        self.layer_visibility = {layer: True for layer in self.layers}
        self.layer_buttons = {}

        for layer in self.layers:
            button = ttk.Button(self, text=layer, command=lambda l=layer: self.set_current_layer(l))
            button.pack(side=tk.LEFT)
            self.layer_buttons[layer] = button

        self.visibility_button = ttk.Button(self, text="Toggle Visibility", command=self.toggle_visibility)
        self.visibility_button.pack(side=tk.LEFT)

    def get_current_layer(self):
        return self.current_layer

    def set_current_layer(self, layer):
        self.current_layer = layer
        for l, button in self.layer_buttons.items():
            if l == layer:
                button.config(state=tk.DISABLED)
            else:
                button.config(state=tk.NORMAL)

    def toggle_visibility(self):
        self.layer_visibility[self.current_layer] = not self.layer_visibility[self.current_layer]
        if self.layer_visibility[self.current_layer]:
            self.canvas.itemconfig(self.current_layer, state='normal')
        else:
            self.canvas.itemconfig(self.current_layer, state='hidden')
