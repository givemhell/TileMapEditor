class UndoRedoManager:
    def __init__(self, output_panel):
        self.output_panel = output_panel
        self.canvas = output_panel.canvas
        self.undo_stack = []
        self.redo_stack = []

    def record_action(self, item_id):
        self.undo_stack.append(item_id)
        self.redo_stack = []  # Clear redo stack after a new action

    def undo(self):
        if self.undo_stack:
            item_id = self.undo_stack.pop()
            self.canvas.delete(item_id)
            self.redo_stack.append(item_id)

    def redo(self):
        if self.redo_stack:
            item_id = self.redo_stack.pop()
            # Assuming the tile data is still available, re-create the image
            # This might need adjustments based on how tile data is stored
            print("Redo functionality needs implementation to recreate the tile.")
