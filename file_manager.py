import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class FileManager(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.output_panel = parent.parent.output_panel
        self.biome_suggestion = parent.parent.biome_suggestion

        self.save_button = ttk.Button(self, text="Save", command=self.save_tilemap)
        self.save_button.pack(side=tk.LEFT)

        self.load_button = ttk.Button(self, text="Load", command=self.load_tilemap)
        self.load_button.pack(side=tk.LEFT)

    def save_tilemap(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 initialfile=self.biome_suggestion.biome_dropdown.get() + "_tilemap.png")
        if file_path:
            print(f"Saving tilemap to {file_path}")
            self.save_canvas_content(file_path)

    def load_tilemap(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if file_path:
            print(f"Loading tilemap from {file_path}")
            self.load_canvas_content(file_path)

    def save_canvas_content(self, file_path):
        # Get the canvas content as an image
        self.output_panel.canvas.update()  # Make sure everything is drawn
        x = self.output_panel.canvas.winfo_rootx()
        y = self.output_panel.canvas.winfo_rooty()
        width = self.output_panel.canvas.winfo_width()
        height = self.output_panel.canvas.winfo_height()

        # Grab the image
        image = Image.grab((x, y, x + width, y + height))
        image.save(file_path)
        print(f"Canvas content saved to {file_path}")

    def load_canvas_content(self, file_path):
        try:
            image = Image.open(file_path)
            self.output_panel.width = image.width
            self.output_panel.height = image.height
            self.output_panel.canvas.config(width=self.output_panel.width, height=self.output_panel.height)
            photo = ImageTk.PhotoImage(image)
            self.output_panel.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.output_panel.canvas.image = photo  # Keep a reference!
            print(f"Canvas content loaded from {file_path}")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
