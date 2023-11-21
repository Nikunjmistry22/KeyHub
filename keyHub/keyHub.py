import tkinter as tk
from features.page1 import Page1
from features.page2 import Page2
from features.page3 import Page3
from features.page4 import Page4
from features.page5 import Page5
from features.page6 import Page6

from tkinter import messagebox
background_color = '#1E1E1E'  # Dark background
nav_bar_color = '#2E2E2E'  # Slightly lighter navigation bar
label_color = '#FFFFFF'  # White text color for labels
highlight_color = '#FF5722'
button_color = '#3498db'

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter GUI")

        # Set background color
        self.root.configure(bg=background_color)

        # Create a frame for the navigation bar with a wider width
        self.nav_frame = tk.Frame(root, width=400, bg=nav_bar_color)
        self.nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Create labels for navigation
        self.label1 = tk.Label(self.nav_frame, text="All Text", font=("Helvetica", 12), padx=20, pady=5, bg=nav_bar_color, fg=label_color)
        self.label2 = tk.Label(self.nav_frame, text="All Files", font=("Helvetica", 12), padx=20, pady=5, bg=nav_bar_color, fg=label_color)
        self.label3 = tk.Label(self.nav_frame, text="All Folders", font=("Helvetica", 12), padx=20, pady=5, bg=nav_bar_color, fg=label_color)
        self.label4 = tk.Label(self.nav_frame, text="Windows Apps", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)
        self.label5 = tk.Label(self.nav_frame, text="Chrome Customization", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)
        self.label6 = tk.Label(self.nav_frame, text="3rd Party Apps", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)

        # Bind click and hover events to labels
        self.label1.bind("<Button-1>", lambda event: self.change_content("All Text"))
        self.label2.bind("<Button-1>", lambda event: self.change_content("All Files"))
        self.label3.bind("<Button-1>", lambda event: self.change_content("All Folders"))
        self.label4.bind("<Button-1>", lambda event: self.change_content("Windows Apps"))
        self.label5.bind("<Button-1>", lambda event: self.change_content("Chrome Customization"))
        self.label6.bind("<Button-1>", lambda event: self.change_content("3rd Party Apps"))

        self.label1.bind("<Enter>", lambda event: self.on_enter(event, self.label1))
        self.label1.bind("<Leave>", lambda event: self.on_leave(event, self.label1))
        self.label2.bind("<Enter>", lambda event: self.on_enter(event, self.label2))
        self.label2.bind("<Leave>", lambda event: self.on_leave(event, self.label2))
        self.label3.bind("<Enter>", lambda event: self.on_enter(event, self.label3))
        self.label3.bind("<Leave>", lambda event: self.on_leave(event, self.label3))
        self.label4.bind("<Enter>", lambda event: self.on_enter(event, self.label4))
        self.label4.bind("<Leave>", lambda event: self.on_leave(event, self.label4))
        self.label5.bind("<Enter>", lambda event: self.on_enter(event, self.label5))
        self.label5.bind("<Leave>", lambda event: self.on_leave(event, self.label5))
        self.label6.bind("<Enter>", lambda event: self.on_enter(event, self.label6))
        self.label6.bind("<Leave>", lambda event: self.on_leave(event, self.label6))

        # Pack labels to the navigation frame
        self.label1.pack(pady=20, anchor='w')
        self.label2.pack(pady=20, anchor='w')
        self.label3.pack(pady=20, anchor='w')
        self.label4.pack(pady=20, anchor='w')
        self.label5.pack(pady=20, anchor='w')
        self.label6.pack(pady=20, anchor='w')

        # Create a frame for the content
        self.content_frame = tk.Frame(root, width=400, height=300, bg=background_color)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Display initial content using Page1
        self.current_content = tk.Label(self.content_frame, text="Welcome to the KeyHub!", font=("Helvetica", 50), padx=20, pady=20, bg=background_color, fg=label_color)
        self.current_content.pack(expand=True)

        self.getting_started_button = tk.Button(self.content_frame, text="Getting Started", font=("Helvetica", 25),bg=button_color, fg=label_color, command=self.getting_started)
        self.getting_started_button.pack(side=tk.BOTTOM, pady=20)

    def change_content(self, page_name):

        # Destroy current content
        if hasattr(self, "page1_instance"):
            self.page1_instance.destroy()
        if hasattr(self, "page2_instance"):
            self.page2_instance.destroy()
        if hasattr(self, "page3_instance"):
            self.page3_instance.destroy()
        if hasattr(self, "page4_instance"):
            self.page4_instance.destroy()
        if hasattr(self, "page5_instance"):
            self.page5_instance.destroy()
        if hasattr(self, "page6_instance"):
            self.page6_instance.destroy()

        self.current_content.destroy()

        # Display new content based on the button clicked
        if page_name == "All Text":
            self.page1_instance = Page1(self.content_frame)
            self.current_content = self.page1_instance.canvas1
            self.getting_started_button.destroy()

        elif page_name == "All Files":
            # Add logic for other pages here
            self.page2_instance = Page2(self.content_frame)
            self.current_content = self.page2_instance.label
            self.getting_started_button.destroy()
            pass
        elif page_name == "All Folders":
            # Add logic for other pages here
            self.page3_instance = Page3(self.content_frame)
            self.current_content = self.page3_instance.canvas3
            self.getting_started_button.destroy()
            pass

        elif page_name == "Windows Apps":
            # Add logic for other pages here
            self.page4_instance = Page4(self.content_frame)
            self.current_content = self.page4_instance.label
            self.getting_started_button.destroy()
            pass

        elif page_name == "Chrome Customization":
            # Add logic for other pages here
            self.page5_instance = Page5(self.content_frame)
            self.current_content = self.page5_instance.canvas1
            self.getting_started_button.destroy()

        elif page_name == "3rd Party Apps":
            # Add logic for other pages here
            self.page6_instance = Page6(self.content_frame)
            self.current_content = self.page6_instance.label
            self.getting_started_button.destroy()

            pass
        self.current_content.pack(expand=True)

    def on_enter(self, event, label):
        label.config(bg=highlight_color)

    def on_leave(self, event, label):
        label.config(bg=nav_bar_color)

    def getting_started(self):
        # Add logic for the "Getting Started" button action
        self.change_content("All Text")
        self.getting_started_button.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGUI(root)
    window_width = 1250
    window_height = 700
    root.geometry(f"{window_width}x{window_height}")
    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"+{x_position}+{y_position}")

    root.mainloop()
