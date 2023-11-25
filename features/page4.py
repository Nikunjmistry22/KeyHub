import tkinter as tk,os,platform
from tkinter import ttk
from tkinter import messagebox,filedialog
import string
background_color = '#1E1E1E'
nav_bar_color = '#2E2E2E'
label_color = '#FFFFFF'
highlight_color = '#FF5722'
button_color = '#3498db'

class Page4:
    def __init__(self, parent_frame):
        from keyHub_test.database.db_connector import SQLiteConnector
        self.parent_frame = parent_frame
        self.counters = {}
        self.title=tk.Label(parent_frame,text="Window Keys",font=("Helvetica",25),bg=background_color,fg=label_color)
        self.title.place(relx=0.5,rely=0.05,anchor="center")
        self.view1 = tk.Button(parent_frame, text="View", font=("Helvetica", 25),
                              bg=button_color, fg=label_color, command=self.view_counters)
        self.view1.place(relx=0.95, rely=0.05, anchor="center")

        self.canvas1 = tk.Canvas(parent_frame, width=400, height=400)
        self.canvas1.pack()
        self.Window_path=""
        self.existing_record = False

        self.i = 1
        self.text_key_label = tk.Label(self.canvas1, text=f"Customize Your Windows ({self.i})", font=("Arial", 12))
        self.text_key_label.place(relx=0.5, rely=0.05, anchor="center")

        self.plus_icon_label = tk.Label(self.canvas1, text="+", font=("Arial", 12))
        self.plus_icon_label.place(relx=0.95, rely=0.05, anchor="ne")
        self.plus_icon_label.bind("<Button-1>", lambda event: self.increment_counter())

        self.minus_icon_label = tk.Label(self.canvas1, text="-", font=("Arial", 12))
        self.minus_icon_label.place(relx=0.1, rely=0.05, anchor="ne")
        self.minus_icon_label.bind("<Button-1>", lambda event: self.decrement_counter())

        self.main_box = tk.LabelFrame(self.canvas1, text="Click anywhere in The Box", width=300, height=300)
        self.main_box.place(relx=0.5, rely=0.5, anchor="center")
        self.main_box.bind("<Button-1>", lambda event: self.open_additional_box())


        self.db_connector = SQLiteConnector("KeyHub.db")
        self.table_name = "CustomizeKeys"
        self.columns = "id INTEGER PRIMARY KEY AUTOINCREMENT, key_id INTEGER not null,category TEXT not null,description TEXT not null, shortcut_key TEXT not null unique"

        self.db_connector.create_table(self.table_name, self.columns)

        # Define variables to store selected values from dropdowns
        self.selected_modifier = tk.StringVar()
        self.selected_key = tk.StringVar()

    def increment_counter(self):
        self.i += 1
        self.text_key_label.config(text=f"Customize Your Windows ({self.i})")

    def destroy(self):
        # Add any additional cleanup code here
        if hasattr(self, 'additional_canvas'):
            self.additional_canvas.destroy()
        if hasattr(self, 'view_canvas1'):
            self.view_canvas1.destroy()
        if hasattr(self, 'add_update_button1'):
            self.add_update_button1.destroy()
        self.canvas1.destroy()
        self.view1.destroy()
        self.title.destroy()

    def decrement_counter(self):
        if self.i > 1:
            self.i -= 1
            self.text_key_label.config(text=f"Customize Your Windows ({self.i})")

    def open_additional_box(self):
        existing_record = self.db_connector.fetch_data(
            f"SELECT * FROM {self.table_name} WHERE key_id=? and category='Window'", (self.i,))

        if existing_record:
            self.existing_record=True
            # Key_id exists, prompt the user
            update_confirmation = tk.messagebox.askyesno("Update Confirmation",
                                                         "Key_id already exists. Do you want to update?")
            if not update_confirmation:
                # User chose not to update, return without updating
                self.increment_counter()
                self.existing_record=False
                return
        self.additional_canvas = tk.Canvas(self.parent_frame, width=300, height=300, bg="lightblue")
        self.additional_canvas.place(relx=0.5, rely=0.5, anchor="center")

        text_key_label = tk.Label(self.additional_canvas, text="Chrome Keys", font=("Arial", 12))
        text_key_label.place(relx=0.5, rely=0.05, anchor="center")

        cross_icon_label = tk.Label(self.additional_canvas, text="x", font=("Arial", 12))
        cross_icon_label.place(relx=0.95, rely=0.05, anchor="ne")

        cross_icon_label.bind("<Button-1>", lambda event: self.close_additional_box(self.additional_canvas))

        self.selected_window = tk.StringVar()

        # Create a Combobox (Dropdown menu)
        self.names = [
            "Microsoft Excel", "Microsoft File Explorer", "Microsoft Word",
            "Microsoft PowerPoint", "Microsoft Notepad",
            "Microsoft Media Player"
        ]
        window_dropdown = ttk.Combobox(self.additional_canvas, textvariable=self.selected_window, font=("Arial", 12),
                                       values=self.names,state="readonly")
        window_dropdown.set("Select Window's Apps")
        window_dropdown.place(relx=0.5, rely=0.35, anchor="center")
        window_dropdown.bind("<<ComboboxSelected>>", self.handle_combobox_selection)

        # Dropdown for modifier keys (Ctrl, Alt, Shift)
        alphanumeric_keys = sorted(list(set(key.upper() for key in string.ascii_letters + string.digits)),
                                   key=lambda x: ord(x))

        modifier_values=['Ctrl', 'Alt', 'Shift']+alphanumeric_keys
        modifier_dropdown = ttk.Combobox(self.additional_canvas, textvariable=self.selected_modifier,
                                         values=modifier_values, state='readonly')
        modifier_dropdown.place(relx=0.7, rely=0.5, anchor="center")
        modifier_label = tk.Label(self.additional_canvas, text="Modifier Key", font=("Arial", 12))
        modifier_label.place(relx=0.3, rely=0.5, anchor="center")

        # Dropdown for regular keys (alphabet, digits)
        # print(alphanumeric_keys)
        key_dropdown = ttk.Combobox(self.additional_canvas, textvariable=self.selected_key,
                                    values=alphanumeric_keys, state='readonly')
        key_dropdown.place(relx=0.7, rely=0.65, anchor="center")
        key_label = tk.Label(self.additional_canvas, text="Regular Key", font=("Arial", 12))
        key_label.place(relx=0.3, rely=0.65, anchor="center")

        clear_btn = tk.Button(self.additional_canvas, text="clear", font=("Arial", 12))
        clear_btn.place(relx=0.4, rely=0.9, anchor="center")

        submit_btn = tk.Button(self.additional_canvas, text="Submit", font=("Arial", 12),
                               command=lambda: self.submit_info(self.Window_path,
                                                               f"{self.selected_modifier.get()}+{self.selected_key.get()}"))
        submit_btn.place(relx=0.6, rely=0.9, anchor="center")

    def handle_combobox_selection(self, event):
        selected_option = self.selected_window.get()
        if selected_option == self.names[0]:
            self.Window_path = self.find_excel_path()
        elif selected_option==self.names[1]:
            self.Window_path=self.find_file_explorer()
        elif selected_option==self.names[2]:
            self.Window_path=self.find_word_path()
        elif selected_option==self.names[3]:
            self.Window_path=self.find_powerpoint_path()
        elif selected_option==self.names[4]:
            self.Window_path=self.find_notepad_path()
        elif selected_option==self.names[5]:
            self.Window_path=self.find_video_player_path()


    def find_excel_path(self):
        office_folder = r"C:\Program Files\Microsoft Office\root"
        office_versions = [d for d in os.listdir(office_folder) if os.path.isdir(os.path.join(office_folder, d))]

        # Find the first folder that starts with "Office"
        for version in office_versions:
            if version.startswith("Office"):
                excel_path = os.path.join(office_folder, version, "EXCEL.EXE")
                if os.path.exists(excel_path):
                    if os.path.exists(excel_path):
                        return os.path.normpath(excel_path).replace("\\", "/")

        return None

    def find_powerpoint_path(self):
        office_folder = r"C:\Program Files\Microsoft Office\root"
        office_versions = [d for d in os.listdir(office_folder) if os.path.isdir(os.path.join(office_folder, d))]

        # Find the first folder that starts with "Office"
        for version in office_versions:
            if version.startswith("Office"):
                powerpoint_path = os.path.join(office_folder, version, "POWERPNT.EXE")
                if os.path.exists(powerpoint_path):
                    return os.path.normpath(powerpoint_path).replace("\\", "/")

        return None

    def find_word_path(self):
        office_folder = r"C:\Program Files\Microsoft Office\root"
        office_versions = [d for d in os.listdir(office_folder) if os.path.isdir(os.path.join(office_folder, d))]

        # Find the first folder that starts with "Office"
        for version in office_versions:
            if version.startswith("Office"):
                word_path = os.path.join(office_folder, version, "WINWORD.EXE")
                if os.path.exists(word_path):
                    return os.path.normpath(word_path).replace("\\", "/")

        return None

    def find_notepad_path(self):
        system32_folder = r"C:\Windows\System32"
        notepad_path = os.path.join(system32_folder, "notepad.exe")

        if os.path.exists(notepad_path):
            return os.path.normpath(notepad_path).replace("\\", "/")
        else:
            return None

    def find_video_player_path(self):
        # Specify the path where common video players are installed
        video_player_paths = [
            "C:\Program Files\Windows Media Player\wmplayer.exe",
            # Add more paths for other video players if needed
        ]

        for path in video_player_paths:
            if os.path.exists(path):
                return os.path.normpath(path).replace("\\", "/")
        print(os.path.normpath(path).replace("\\", "/"))
        return None

    def find_file_explorer(self):
        return 'explorer'


    def submit_info(self, description_text, shortcut_text):
        try:
            shortcut_keys = [
                'Ctrl+C', 'Ctrl+X', 'Ctrl+V', 'Ctrl+Z', 'Ctrl+Y', 'Ctrl+A',
                'Ctrl+F', 'Ctrl+S', 'Ctrl+N', 'Ctrl+O', 'Ctrl+P', 'Ctrl+W',
                'Ctrl+Q', 'Ctrl+E', 'Ctrl+Shift+N', 'Ctrl+Shift+Esc', 'Alt+Tab',
                'Alt+F4', 'Windows key+D', 'Windows key+L', 'Windows key+E', 'Windows key+R',
                'Shift+C', 'Shift+M', 'Shift+W', 'Shift+F'
            ]

            # Check if the shortcut_key already exists
            if shortcut_text in shortcut_keys:
                tk.messagebox.showinfo("Windows Default Shortcut Key",
                                       "The ShortCut key u selected is a default Windows Shortcut Key.")
                return
            # Check if the shortcut_key already exists
            existing_record = self.db_connector.fetch_data(
                f"SELECT * FROM {self.table_name} WHERE shortcut_key=?", (shortcut_text,))

            if existing_record:
                # Shortcut_key already exists, show a messagebox
                tk.messagebox.showinfo("Shortcut Key Exists", "Shortcut Key already exists. Choose a different one.")
            else:
                # Shortcut_key doesn't exist, proceed with update or insert
                if self.existing_record:
                    # Key_id exists, update the existing record
                    update_query = f"UPDATE {self.table_name} SET description=?, shortcut_key=? WHERE key_id=? and category=? "
                    update_params = (description_text, shortcut_text, self.i,'Window')
                    self.db_connector.execute_query(update_query, update_params)
                else:
                    # Key_id doesn't exist, insert a new record
                    insert_query = f"INSERT INTO {self.table_name} (key_id, category, description, shortcut_key) VALUES (?, ?, ?, ?)"
                    insert_params = (self.i, 'Window', description_text, shortcut_text)
                    self.db_connector.execute_query(insert_query, insert_params)
                # If no exception is raised, show a success message
                tk.messagebox.showinfo("Success", "Record successfully inserted/updated.")
        except Exception as e:
            # If an exception occurs, show an error message
            error_message = f"An error occurred: {str(e)}"
            tk.messagebox.showerror("Error", error_message)
    def close_additional_box(self, additional_canvas):
        additional_canvas.destroy()

    def view_counters(self):
        self.canvas1.destroy()
        self.view1.destroy()
        # Create the view_canvas
        self.view_canvas1 = tk.Canvas(self.parent_frame, width=900, height=700)
        self.view_canvas1.place(relx=0.5, rely=0.5, anchor="center")
        query = f"SELECT * FROM {self.table_name} where category='Window' order by key_id;"
        results = self.db_connector.fetch_data(query)

        text_widget = tk.Text(self.view_canvas1, wrap=tk.WORD, width=80, height=20)

        text_widget.pack()

        for row in results:
            text_widget.insert(tk.END, f"Counter Value: {row[1]}\n")
            text_widget.insert(tk.END, f"Description: {row[3]}\n")
            text_widget.insert(tk.END, f"Shortcut_keys: {row[4]}\n\n")

        self.add_update_button1 = tk.Button(self.parent_frame, text="Add/Update", font=("Helvetica", 25),
                                           bg=button_color, fg=label_color, command=self.back_to_main_canvas)
        self.add_update_button1.place(relx=0.9, rely=0.05, anchor="center")

    def back_to_main_canvas(self):
        self.view_canvas1.destroy()
        self.add_update_button1.destroy()
        self.view1 = tk.Button(self.parent_frame, text="View", font=("Helvetica", 25),
                              bg=button_color, fg=label_color, command=self.view_counters)
        self.view1.place(relx=0.95, rely=0.05, anchor="center")

        self.canvas1 = tk.Canvas(self.parent_frame, width=400, height=400)
        self.canvas1.place(relx=0.5, rely=0.5, anchor="center")

        self.i = 1
        self.text_key_label = tk.Label(self.canvas1, text=f"Customize Your Windows ({self.i})", font=("Arial", 12))
        self.text_key_label.place(relx=0.5, rely=0.05, anchor="center")

        self.plus_icon_label = tk.Label(self.canvas1, text="+", font=("Arial", 12))
        self.plus_icon_label.place(relx=0.95, rely=0.05, anchor="ne")
        self.plus_icon_label.bind("<Button-1>", lambda event: self.increment_counter())

        self.minus_icon_label = tk.Label(self.canvas1, text="-", font=("Arial", 12))
        self.minus_icon_label.place(relx=0.1, rely=0.05, anchor="ne")
        self.minus_icon_label.bind("<Button-1>", lambda event: self.decrement_counter())

        self.main_box = tk.LabelFrame(self.canvas1, text="Click anywhere in The Box", width=300, height=300)
        self.main_box.place(relx=0.5, rely=0.5, anchor="center")
        self.main_box.bind("<Button-1>", lambda event: self.open_additional_box())

        self.view1.place(relx=0.95, rely=0.05, anchor="center")
