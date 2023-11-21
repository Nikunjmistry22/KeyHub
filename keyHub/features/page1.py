import tkinter as tk
from tkinter import ttk
from keyHub_test.database.db_connector import SQLiteConnector

background_color = '#1E1E1E'
nav_bar_color = '#2E2E2E'
label_color = '#FFFFFF'
highlight_color = '#FF5722'
button_color = '#3498db'

class Page1:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.counters = {}
        self.title=tk.Label(parent_frame,text="Text Keys",font=("Helvetica",25),bg=background_color,fg=label_color)
        self.title.place(relx=0.5,rely=0.05,anchor="center")
        self.view1 = tk.Button(parent_frame, text="View", font=("Helvetica", 25),
                              bg=button_color, fg=label_color, command=self.view_counters)
        self.view1.place(relx=0.95, rely=0.05, anchor="center")

        self.canvas1 = tk.Canvas(parent_frame, width=400, height=400)
        self.canvas1.pack()
        self.existing_record = False

        self.i = 1
        self.text_key_label = tk.Label(self.canvas1, text=f"Customize the text keys ({self.i})", font=("Arial", 12))
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
        self.columns = "id INTEGER PRIMARY KEY AUTOINCREMENT, key_id INTEGER not null,category TEXT not null,description TEXT not null, shortcut_key TEXT not null"

        self.db_connector.create_table(self.table_name, self.columns)

        # Define variables to store selected values from dropdowns
        self.selected_modifier = tk.StringVar()
        self.selected_key = tk.StringVar()

    def increment_counter(self):
        self.i += 1
        self.text_key_label.config(text=f"Customize the text keys ({self.i})")

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
            self.text_key_label.config(text=f"Customize the text keys ({self.i})")

    def open_additional_box(self):
        existing_record = self.db_connector.fetch_data(
            f"SELECT * FROM {self.table_name} WHERE key_id=? and category='Text'", (self.i,))

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

        text_key_label = tk.Label(self.additional_canvas, text="Text Customize Key", font=("Arial", 12))
        text_key_label.place(relx=0.5, rely=0.05, anchor="center")

        cross_icon_label = tk.Label(self.additional_canvas, text="x", font=("Arial", 12))
        cross_icon_label.place(relx=0.95, rely=0.05, anchor="ne")

        cross_icon_label.bind("<Button-1>", lambda event: self.close_additional_box(self.additional_canvas))

        label_text = tk.Label(self.additional_canvas, text="Description", font=("Arial", 12))
        label_text.place(relx=0.3, rely=0.35, anchor="center")

        text_input = tk.Entry(self.additional_canvas, font=("Arial", 12), width=15)
        text_input.place(relx=0.7, rely=0.35, anchor="center")

        # Dropdown for modifier keys (Ctrl, Alt, Shift)
        modifier_dropdown = ttk.Combobox(self.additional_canvas, textvariable=self.selected_modifier,
                                         values=['Ctrl', 'Alt', 'Shift'], state='readonly')
        modifier_dropdown.place(relx=0.7, rely=0.5, anchor="center")
        modifier_label = tk.Label(self.additional_canvas, text="Modifier Key", font=("Arial", 12))
        modifier_label.place(relx=0.3, rely=0.5, anchor="center")

        # Dropdown for regular keys (alphabet, digits)
        key_dropdown = ttk.Combobox(self.additional_canvas, textvariable=self.selected_key,
                                    values=['A', 'B', 'C', '1', '2', '3'], state='readonly')
        key_dropdown.place(relx=0.7, rely=0.65, anchor="center")
        key_label = tk.Label(self.additional_canvas, text="Regular Key", font=("Arial", 12))
        key_label.place(relx=0.3, rely=0.65, anchor="center")

        clear_btn = tk.Button(self.additional_canvas, text="clear", font=("Arial", 12))
        clear_btn.place(relx=0.4, rely=0.9, anchor="center")

        submit_btn = tk.Button(self.additional_canvas, text="Submit", font=("Arial", 12),
                               command=lambda: self.submit_info(text_input.get(),
                                                               f"{self.selected_modifier.get()}+{self.selected_key.get()}"))
        submit_btn.place(relx=0.6, rely=0.9, anchor="center")

    def submit_info(self, description_text, shortcut_text):
        # Store the information in the dictionary
        self.counters[self.i] = {'description_text': description_text, 'shortcut_text': shortcut_text}

        if self.existing_record:
            # Key_id exists, update the existing record
            update_query = f"UPDATE {self.table_name} SET category=?, description=?, shortcut_key=? WHERE key_id=? and category='Text'"
            update_params = ('Text', description_text, shortcut_text, self.i)
            self.db_connector.execute_query(update_query, update_params)
        else:
            # Key_id doesn't exist, insert a new record
            insert_query = f"INSERT INTO {self.table_name} (key_id, category, description, shortcut_key) VALUES (?, ?, ?, ?)"
            insert_params = (self.i, 'Text', description_text, shortcut_text)
            self.db_connector.execute_query(insert_query, insert_params)

    def close_additional_box(self, additional_canvas):
        additional_canvas.destroy()

    def view_counters(self):
        self.canvas1.destroy()
        self.view1.destroy()
        # Create the view_canvas
        self.view_canvas1 = tk.Canvas(self.parent_frame, width=900, height=700)
        self.view_canvas1.place(relx=0.5, rely=0.5, anchor="center")
        query = f"SELECT * FROM {self.table_name} where category='Text';"
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
        self.text_key_label = tk.Label(self.canvas1, text=f"Customize the text keys ({self.i})", font=("Arial", 12))
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