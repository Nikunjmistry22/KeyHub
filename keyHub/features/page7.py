import tkinter as tk
background_color = '#1E1E1E'
label_color = '#FFFFFF'
toggle_off_color = '#3498db'
toggle_on_color = '#000000'
hover_color = '#FFA500'

class Page7:
    def __init__(self, parent_frame):
        self.title = tk.Label(parent_frame, text="About", font=("Helvetica", 25), bg=background_color,
                              fg=label_color)
        self.title.place(relx=0.52, rely=0.05, anchor="center")
        self.canvas1 = tk.Canvas(parent_frame, width=700, height=500, bg=background_color)
        self.canvas1.pack()

        self.notification = tk.Label(self.canvas1, text="Notification Shortcut Keys", font=("Helvetica", 25),
                                     bg=background_color, fg=label_color)
        self.notification.place(relx=0.5, rely=0.05, anchor="center")

        self.file = tk.Label(self.canvas1, text="File Shortcuts", font=("Helvetica", 15), bg=background_color,
                             fg=label_color)
        self.file.place(relx=0.05, rely=0.3, anchor="w")
        self.file_key = tk.Label(self.canvas1, text="Shift+M", font=("Helvetica", 15), bg=background_color,
                                 fg=label_color)
        self.file_key.place(relx=0.95, rely=0.3, anchor="e")

        self.folder = tk.Label(self.canvas1, text="Folder Shortcuts", font=("Helvetica", 15), bg=background_color,
                               fg=label_color)
        self.folder.place(relx=0.05, rely=0.4, anchor="w")
        self.folder_key = tk.Label(self.canvas1, text="Shift+F", font=("Helvetica", 15), bg=background_color,
                                   fg=label_color)
        self.folder_key.place(relx=0.95, rely=0.4, anchor="e")

        self.chrome = tk.Label(self.canvas1, text="Chrome Shortcuts", font=("Helvetica", 15), bg=background_color,
                               fg=label_color)
        self.chrome.place(relx=0.05, rely=0.5, anchor="w")
        self.chrome_key = tk.Label(self.canvas1, text="Shift+C", font=("Helvetica", 15), bg=background_color,
                                   fg=label_color)
        self.chrome_key.place(relx=0.95, rely=0.5, anchor="e")
        self.window = tk.Label(self.canvas1, text="Window Shortcuts", font=("Helvetica", 15), bg=background_color,
                               fg=label_color)
        self.window.place(relx=0.05, rely=0.6, anchor="w")
        self.window_key = tk.Label(self.canvas1, text="Shift+W", font=("Helvetica", 15), bg=background_color,
                                   fg=label_color)
        self.window_key.place(relx=0.95, rely=0.6, anchor="e")
        self.end = tk.Label(self.canvas1, text="Disable Customized Shortcuts on window close", font=("Helvetica", 15), bg=background_color,
                               fg=label_color)
        self.end.place(relx=0.05, rely=0.6, anchor="w")
        self.end_key = tk.Label(self.canvas1, text="Esc+Esc", font=("Helvetica", 15), bg=background_color,
                                   fg=label_color)
        self.end_key.place(relx=0.95, rely=0.6, anchor="e")


        self.copyright_text = tk.Label(parent_frame, text="@Copyright Nikunj Mistry 2023", font=("Helvetica", 15),
                                       bg=background_color, fg=label_color)
        self.copyright_text.place(relx=0.5, rely=0.8, anchor="center")
    def destroy(self):
        self.canvas1.destroy()
        self.title.destroy()
        self.copyright_text.destroy()

