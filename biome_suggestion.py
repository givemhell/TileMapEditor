import tkinter as tk
from tkinter import ttk

class BiomeSuggestion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.biome_label = ttk.Label(self, text="Suggested Biome: ")
        self.biome_label.pack(side=tk.LEFT)
        self.biome_dropdown = ttk.Combobox(self, values=["Grass", "Fire", "Water", "Cave", "Snow", "Desert"])
        self.biome_dropdown.pack(side=tk.LEFT)
        self.biome_dropdown.set("Grass")  # Default biome
