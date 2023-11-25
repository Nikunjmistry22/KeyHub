import tkinter as tk
from features.page2 import Page2
from features.page3 import Page3
from features.page4 import Page4
from features.page5 import Page5
from features.page7 import Page7
from multiprocessing import Process,freeze_support
import keyboard
from keyHub_test.database.db_connector import SQLiteConnector

def run_automate_shortcut():
    db_connector = SQLiteConnector("KeyHub.db")
    from automate_shortcut import register_hotkeys
    try:
        register_hotkeys()
        keyboard.wait('esc')
    except KeyboardInterrupt:
        pass
    finally:
        db_connector.close_connection()


if __name__ == '__main__':
    freeze_support()
    shortcut_process = Process(target=run_automate_shortcut)
    shortcut_process.start()
    background_color = '#1E1E1E'
    nav_bar_color = '#2E2E2E'
    label_color = '#FFFFFF'
    highlight_color = '#FF5722'
    button_color = '#3498db'
    class keyHub:
        def __init__(self, root):
            from keyHub_test.database.db_connector import SQLiteConnector
            self.root = root
            root.bind("<Escape>", self.stop_automate_script)
            self.root.configure(bg=background_color)

            self.nav_frame = tk.Frame(root, width=400, bg=nav_bar_color)
            self.nav_frame.pack(side=tk.LEFT, fill=tk.Y)

            self.label2 = tk.Label(self.nav_frame, text="All Files", font=("Helvetica", 12), padx=20, pady=5, bg=nav_bar_color, fg=label_color)
            self.label3 = tk.Label(self.nav_frame, text="All Folders", font=("Helvetica", 12), padx=20, pady=5, bg=nav_bar_color, fg=label_color)
            self.label4 = tk.Label(self.nav_frame, text="Windows Apps", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)
            self.label5 = tk.Label(self.nav_frame, text="Chrome Customization", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)
            self.label7 = tk.Label(self.nav_frame, text="About keyHub", font=("Helvetica", 12), padx=20, pady=5,bg=nav_bar_color, fg=label_color)

            # Bind click and hover events to labels
            self.label2.bind("<Button-1>", lambda event: self.change_content("All Files"))
            self.label3.bind("<Button-1>", lambda event: self.change_content("All Folders"))
            self.label4.bind("<Button-1>", lambda event: self.change_content("Windows Apps"))
            self.label5.bind("<Button-1>", lambda event: self.change_content("Chrome Customization"))
            self.label7.bind("<Button-1>", lambda event: self.change_content("About keyHub"))

            self.label2.bind("<Enter>", lambda event: self.on_enter(event, self.label2))
            self.label2.bind("<Leave>", lambda event: self.on_leave(event, self.label2))
            self.label3.bind("<Enter>", lambda event: self.on_enter(event, self.label3))
            self.label3.bind("<Leave>", lambda event: self.on_leave(event, self.label3))
            self.label4.bind("<Enter>", lambda event: self.on_enter(event, self.label4))
            self.label4.bind("<Leave>", lambda event: self.on_leave(event, self.label4))
            self.label5.bind("<Enter>", lambda event: self.on_enter(event, self.label5))
            self.label5.bind("<Leave>", lambda event: self.on_leave(event, self.label5))
            self.label7.bind("<Enter>", lambda event: self.on_enter(event, self.label7))
            self.label7.bind("<Leave>", lambda event: self.on_leave(event, self.label7))

            # Pack labels to the navigation frame
            self.label2.pack(pady=20, anchor='w')
            self.label3.pack(pady=20, anchor='w')
            self.label4.pack(pady=20, anchor='w')
            self.label5.pack(pady=20, anchor='w')
            self.label7.pack(pady=20, anchor='w')

            self.content_frame = tk.Frame(root, width=400, height=300, bg=background_color)
            self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            # Display initial content using Page1
            self.current_content = tk.Label(self.content_frame, text="KeyHub", font=("Helvetica", 50), bg=background_color, fg=label_color)
            self.current_content.place(relx=0.4,rely=0.3)

            self.current_content = tk.Label(self.content_frame, text="** Customize Your Shortcuts with Ease **", font=("Helvetica", 15),  bg=background_color, fg=label_color)
            self.current_content.place(relx=0.33, rely=0.45)

            self.getting_started_button = tk.Button(self.content_frame, text="Getting Started", font=("Helvetica", 25),bg=button_color, fg=label_color, command=self.getting_started)
            self.getting_started_button.pack(side=tk.BOTTOM, pady=20)

            self.db_connector = SQLiteConnector("KeyHub.db")
            self.table_name = "CustomizeKeys"
            self.columns = "id INTEGER PRIMARY KEY AUTOINCREMENT, key_id INTEGER not null,category TEXT not null,description TEXT not null, shortcut_key TEXT not null unique"

            self.db_connector.create_table(self.table_name, self.columns)
        def stop_automate_script(self, event):
            shortcut_process.terminate()
            shortcut_process.join()
            root.destroy()

        def change_content(self, page_name):

            # Destroy current content
            if hasattr(self, "page2_instance"):
                self.current_content.destroy()
                self.page2_instance.destroy()
            if hasattr(self, "page3_instance"):
                self.current_content.destroy()
                self.page3_instance.destroy()
            if hasattr(self, "page4_instance"):
                self.current_content.destroy()
                self.page4_instance.destroy()
            if hasattr(self, "page5_instance"):
                self.current_content.destroy()
                self.page5_instance.destroy()
            if hasattr(self, "page6_instance"):
                self.current_content.destroy()
                self.page6_instance.destroy()
            if hasattr(self, "page7_instance"):
                self.current_content.destroy()
                self.page7_instance.destroy()
            self.current_content.destroy()


            if page_name == "All Files":
                self.page2_instance = Page2(self.content_frame)
                self.current_content = self.page2_instance.canvas1
                self.getting_started_button.destroy()
                pass

            elif page_name == "All Folders":
                self.page3_instance = Page3(self.content_frame)
                self.current_content = self.page3_instance.canvas1
                self.getting_started_button.destroy()
                pass

            elif page_name == "Windows Apps":
                self.page4_instance = Page4(self.content_frame)
                self.current_content = self.page4_instance.canvas1
                self.getting_started_button.destroy()
                pass

            elif page_name == "Chrome Customization":
                self.page5_instance = Page5(self.content_frame)
                self.current_content = self.page5_instance.canvas1
                self.getting_started_button.destroy()

            elif page_name == "About keyHub":
                self.page7_instance = Page7(self.content_frame)
                self.current_content = self.page7_instance.canvas1
                self.getting_started_button.destroy()


            self.current_content.pack(expand=True)

        def on_enter(self, event, label):
            label.config(bg=highlight_color)

        def on_leave(self, event, label):
            label.config(bg=nav_bar_color)

        def getting_started(self):

            self.change_content("Chrome Customization")
            self.getting_started_button.destroy()


    def on_close():
        shortcut_process.terminate()
        shortcut_process.join()
        root.destroy()


    try:
        if __name__ == "__main__":
            root = tk.Tk()
            app = keyHub(root)
            window_width = 1250
            window_height = 700
            root.geometry(f"{window_width}x{window_height}")

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2
            root.geometry(f"+{x_position}+{y_position}")

            root.protocol("WM_DELETE_WINDOW", on_close)

            root.mainloop()

            new_shortcut_process = Process(target=run_automate_shortcut)
            new_shortcut_process.start()

    except KeyboardInterrupt:
        shortcut_process.terminate()
        shortcut_process.join()
