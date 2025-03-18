import tkinter as tk
from tkinter import ttk
from input_panel import InputPanel
from output_panel import OutputPanel
from toolbar import Toolbar
from biome_suggestion import BiomeSuggestion

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Tilemap Editor")

        self.biome_suggestion = BiomeSuggestion(self.root)
        self.biome_suggestion.pack(side=tk.TOP, fill=tk.X)

        self.output_panel = OutputPanel(self.root)
        self.output_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.input_panel = InputPanel(self.root)
        self.input_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.toolbar = Toolbar(self.root, self.output_panel)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
