import tkinter as tk
from tkinter import messagebox
background_color = '#1E1E1E'
label_color = '#FFFFFF'
toggle_off_color = '#3498db'
toggle_on_color = '#000000'
hover_color = '#FFA500'  # Adjust the hover color as needed

class Page7:
    def __init__(self, parent_frame):
        self.title = tk.Label(parent_frame, text="Settings", font=("Helvetica", 25), bg=background_color, fg=label_color)
        self.title.place(relx=0.5, rely=0.05, anchor="center")
        self.canvas1 = tk.Canvas(parent_frame, width=700, height=500, bg=background_color)
        self.canvas1.pack()

        # Add a custom circular toggle button
        self.toggle_var = tk.BooleanVar(value=True)  # Set the initial value to True
        self.toggle_button = tk.Canvas(self.canvas1, width=40, height=40, highlightthickness=0, bd=0, bg=background_color)
        self.toggle_button.place(relx=0.95, rely=0.05, anchor="center")

        self.draw_toggle_button()

        # Bind the button click event
        self.toggle_button.bind("<Button-1>", self.toggle_feature)

        # Set the initial heading label text
        self.toggle_feature()

        self.notification = tk.Label(self.canvas1, text="Notification Shortcut Keys", font=("Helvetica", 25), bg=background_color,
                              fg=label_color)

        self.notification.place(relx=0.5, rely=0.05, anchor="center")
        self.file = tk.Label(self.canvas1, text="File Shortcuts", font=("Helvetica", 20),bg=background_color,fg=label_color)
        self.file.place(relx=0.05, rely=0.3, anchor="w")
        self.file_key = tk.Label(self.canvas1, text="Shift+M", font=("Helvetica", 20),bg=background_color,fg=label_color)
        self.file_key.place(relx=0.95, rely=0.3, anchor="e")

        self.folder = tk.Label(self.canvas1, text="Folder Shortcuts", font=("Helvetica", 20), bg=background_color,
                             fg=label_color)
        self.folder.place(relx=0.05, rely=0.5, anchor="w")
        self.folder_key = tk.Label(self.canvas1, text="Shift+F", font=("Helvetica", 20), bg=background_color,
                                 fg=label_color)
        self.folder_key.place(relx=0.95, rely=0.5, anchor="e")

        self.chrome = tk.Label(self.canvas1, text="Chrome Shortcuts", font=("Helvetica", 20), bg=background_color,
                             fg=label_color)
        self.chrome.place(relx=0.05, rely=0.7, anchor="w")
        self.chrome_key = tk.Label(self.canvas1, text="Shift+C", font=("Helvetica", 20), bg=background_color,
                                 fg=label_color)
        self.chrome_key.place(relx=0.95, rely=0.7, anchor="e")
        self.window = tk.Label(self.canvas1, text="Window Shortcuts", font=("Helvetica", 20), bg=background_color,
                             fg=label_color)
        self.window.place(relx=0.05, rely=0.9, anchor="w")
        self.window_key = tk.Label(self.canvas1, text="Shift+W", font=("Helvetica", 20), bg=background_color,
                                 fg=label_color)
        self.window_key.place(relx=0.95, rely=0.9, anchor="e")


    def draw_toggle_button(self):
        color = toggle_on_color if self.toggle_var.get() else toggle_off_color
        self.toggle_button.delete("all")
        self.toggle_button.create_oval(0, 0, 40, 40, fill=color, outline="")

    def toggle_feature(self, event=None):
        self.toggle_var.set(not self.toggle_var.get())
        self.draw_toggle_button()


    def destroy(self):
        # Add any additional cleanup code here
        self.canvas1.destroy()
        self.title.destroy()

