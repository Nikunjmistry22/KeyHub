import tkinter as tk

class Page3:
    def __init__(self, parent_frame):
        self.label = tk.Label(parent_frame, text="This is Page 3", font=("Helvetica", 16), padx=20, pady=20)
    def destroy(self):
        # Add any additional cleanup code here
        self.label.destroy()
        # self.view1.destroy()