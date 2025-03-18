import tkinter as tk
from tkinter import ttk

class TilePropertiesPanel(ttk.Frame):
    def __init__(self, parent, tile_properties):
        super().__init__(parent)
        self.parent = parent
        self.tile_properties = tile_properties
        self.tile_id = None

        self.collision_label = ttk.Label(self, text="Collision:")
        self.collision_label.pack()
        self.collision_var = tk.StringVar()
        self.collision_entry = ttk.Entry(self, textvariable=self.collision_var)
        self.collision_entry.pack()

        self.interaction_label = ttk.Label(self, text="Interaction:")
        self.interaction_label.pack()
        self.interaction_var = tk.StringVar()
        self.interaction_entry = ttk.Entry(self, textvariable=self.interaction_var)
        self.interaction_entry.pack()

        self.object_type_label = ttk.Label(self, text="Object Type:")
        self.object_type_label.pack()
        self.object_type_var = tk.StringVar()
        self.object_type_entry = ttk.Entry(self, textvariable=self.object_type_var)
        self.object_type_entry.pack()

        self.save_button = ttk.Button(self, text="Save Properties", command=self.save_properties)
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
