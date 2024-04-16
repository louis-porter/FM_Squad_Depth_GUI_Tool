from data_loader import DataLoader
import tkinter as tk
from tkinter import ttk



class RoleDropdown:
    def __init__(self, parent_canvas):
        self.canvas = parent_canvas
        self.dataloader = DataLoader()
        self.roles = self.dataloader.role_list

    def show_dropdown(self, x, y, callback):

        self.abs_x = x
        self.abs_y = y

        self.dropdown_window = tk.Toplevel(self.canvas)
        self.dropdown_window.wm_overrideredirect(True)
        self.dropdown_window.geometry(f"+{self.abs_x}+{self.abs_y}")

        self.selected_position = tk.StringVar(self.dropdown_window)
        self.combobox = ttk.Combobox(self.dropdown_window, textvariable=self.selected_position, state="readonly")
        self.combobox["values"] = self.roles
        self.combobox.set("Select a role")
        self.combobox.pack(fill="both", expand=True)
        self.combobox.bind("<<ComboboxSelected>>", lambda event: self.on_role_select(event, callback))

    def on_role_select(self, event, callback):
        self.role_selected = self.selected_position.get()
        self.dropdown_window.destroy()
        callback(self.role_selected)

    

        

        

    