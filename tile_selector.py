from PIL import Image

class TileSelector:
    def __init__(self, canvas, input_panel):
        self.canvas = canvas
        self.input_panel = input_panel
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.selection_rect = None

    def start_selection(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.end_x = event.x
        self.end_y = event.y
        self.selection_rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def update_selection(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.canvas.coords(self.selection_rect, self.start_x, self.start_y, self.end_x, self.end_y)

    def end_selection(self, event):
        self.end_x = event.x
        self.end_y = event.y
        self.canvas.delete(self.selection_rect)
        
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)

        self.select_tile(x1, y1, x2, y2)

    def select_tile(self, x1, y1, x2, y2):
        try:
            image = self.input_panel.image
            selected_tile = image.crop((x1, y1, x2, y2))
            self.input_panel.set_selected_tile(selected_tile)
            print(f"Selected area: ({x1}, {y1}) to ({x2}, {y2})")
        except Exception as e:
            print(f"Error selecting tile: {e}")
